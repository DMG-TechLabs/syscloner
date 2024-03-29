import shutil
import os
import subprocess
from logger import debu


def run_shell_command(command):
    result = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)

    return result.stdout.strip() if result.returncode == 0 else ""


def get_bytes(file):
    """
    Returns
    -------
    bytes
        file contents
    """

    temp = ""
    with open(file, "rb") as filename:
        temp = filename.read()
        filename.close()
    return temp


def get_apt_packages():
    """
    Returns
    -------
    list
        apt packages
    """

    result = run_shell_command(['apt', 'list', '--installed'])
    package_names = [line.split('/')[0] for line in result.split('\n') if line.strip()]

    return package_names


def get_apt_repos():
    """
    Returns
    -------
    list
        apt repositories as [path, line, line, ...]
    """

    apt_repos = list()

    result = subprocess.run(['egrep', '-r', '^deb.*', '/etc/apt/'], stdout=subprocess.PIPE)
    apt_repos_paths_urls = str(result.stdout).replace("b'", "").replace("'", "").split("\\n")

    result = subprocess.run(['egrep', '-rl', '^deb.*', '/etc/apt/'], stdout=subprocess.PIPE)
    apt_repos_paths = str(result.stdout).replace("b'", "").replace("'", "").split("\\n")

    result = subprocess.run(['egrep', '-r', '-h', '^deb.*', '/etc/apt/'], stdout=subprocess.PIPE)
    apt_repos_urls = str(result.stdout).replace("b'", "").replace("'", "").split("\\n")

    for i in range(len(apt_repos_paths) - 1):
        apt_repos.append([apt_repos_paths[i]])
        for j in range(len(apt_repos_paths_urls)):
            for k in range(len(apt_repos_urls)):
                string = str()
                string = apt_repos_paths[i] + ":" + apt_repos_urls[k]
                if string == apt_repos_paths_urls[j]:
                    apt_repos[i] = apt_repos[i] + [apt_repos_urls[k]]

    # Clean double lines
    cleaned_repos = []
    for repo in apt_repos:
        cleaned_repo = [repo[i] for i in range(len(repo)) if i == 0 or repo[i] != repo[i-1]]
        cleaned_repos.append(cleaned_repo)

    return cleaned_repos

def get_gnome_extensions():
    """
    Returns
    -------
    list
        gnome extensions
    """

    extensions = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    extensions = str(extensions.stdout).replace("b'", "").replace("'", "")
    lst = extensions.split("\\n")
    lst.remove('')
    return lst



def get_flatpak_packages():
    """
    Returns
    -------
    list
        flatpak packages
    """

    result = run_shell_command(['flatpak', 'list'])
    package_names = [line.split('\t', 1)[0] for line in result.split('\n') if line.strip()]

    return package_names


def get_snap_packages():
    """
    Returns
    -------
    list
        snap packages
    """

    result = run_shell_command(['snap', 'list'])
    package_names = [line.split()[0] for line in result.split('\n')[1:] if line.strip()]

    return package_names


def get_sources_keys():
    """
    Returns apt gpg keys

    Returns
    -------
    list of [path, bytes]
        apt source keys
    """

    files = []
    sources = []
    w = os.walk("/etc/apt")
    for root, dirs, files_list in w:
        for file in files_list:
            if file.endswith(".gpg") or file.endswith(".asc"):
                files.append(os.path.join(root, file))

    for i in range(0, len(files)-1):
        file = files[i]
        with open(file, "rb") as filename:
            sources.append([])
            sources[i].append(file)
            sources[i].append(filename.read())
            filename.close()
    return sources


def get_ssh_keys():
    """
    Returns all ssh files and their contents

    Returns
    -------
    list
        ssh files as [path, contents]
    """

    files = []
    sources = []
    home = os.path.expanduser('~')
    w = os.walk(home + "/.ssh")
    for root, dirs, files_list in w:
        files = files_list

    for i in range(0, len(files)-1):
        filename = files[i]

        contents = ""
        try:
            with open(f'{home}/.ssh/{filename}', 'rb') as file:
                try:
                    contents = file.read().decode('utf-8')
                except UnicodeDecodeError:
                    try_encodings = ['latin-1', 'utf-16']
                    for encoding in try_encodings:
                        try:
                            contents = file.read().decode(encoding)
                            break
                        except UnicodeDecodeError:
                            continue
                    else:
                        return []
        except FileNotFoundError:
            print(f"File '{filename}' not found in ~/.ssh directory.")

        sources.append([])
        sources[i].append(filename)
        sources[i].append(str(contents))

    for source in sources:
        source[0] = "~/.ssh/" + source[0]

    return sources


def get_shell_themes():
    """
    Returns
    -------
    bytes
        the zipped shell themes
    """

    data = b""
    name = os.path.expanduser('~')+"/shell-themes-cvf"
    shutil.make_archive(name, 'gztar', "/usr/share/themes")
    with open(name+".tar.gz", "rb") as file:
        data = file.read()
        file.close()

    os.remove(name+".tar.gz")
    return data


def get_dconf():
    """
    Returns
    -------
    bytes
        the dconf file
    """

    return get_bytes(os.path.expanduser('~')+"/.config/dconf/user")


def is_substring_in_list(substring, string_list):
    for string in string_list:
        if substring in string:
            return True
    return False


def substring_in_list(substring, string_list):
    for string in string_list:
        if substring in string:
            return string
    return ""


def get_git_repos(path):
    """
    Returns all the git repos that have a remote, starting from a specific
    path. The method excludes git submodules.

    Returns
    -------
    list
        git repos as [path, remote-url]
    """

    path = path or "$HOME"  # I dont know if this works


    git_repos = list()
    not_valid_repos = []
    lines = []

    for root, dirs, files in os.walk(path):
        for d in dirs:
            full_dir_path = os.path.join(root, d)

            if(is_substring_in_list(full_dir_path, not_valid_repos)): continue

            git_dir = os.path.join(full_dir_path, '.git')

            if os.path.exists(git_dir):
                git_output = run_shell_command(['git', '-C', full_dir_path, 'rev-parse', '--is-inside-work-tree'])

                if git_output == "true":
                    repo_url = run_shell_command(['git', '-C', full_dir_path, 'config', '--get', 'remote.origin.url'])
                    
                    if repo_url != "":
                        git_repos.append([os.path.normpath(full_dir_path), repo_url])
            
            submodule_path = os.path.join(full_dir_path, '.gitmodules')
            if(os.path.exists(submodule_path)):
                not_valid_repos.append(full_dir_path)
                with open(submodule_path, 'r') as file:
                    lines = file.readlines()
                    file.close()
                if(substring_in_list("path", lines) != ""):  
                    not_valid_repos.append(full_dir_path+"/"+substring_in_list("path", lines).replace("\t", "").replace("path = ",""))
                continue

    for pair in git_repos:
        pair[0] = pair[0].replace(os.path.expanduser('~'), "~")

    return git_repos
