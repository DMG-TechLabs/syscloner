from constants import SSH


from pdb import run
import shutil
import os
import subprocess


def get_bytes(file):
    """
    Returns file contents as bytes
    """

    temp = ""
    with open(file, "rb") as filename:
        temp = filename.read() 
        filename.close()
    return temp


def get_packages(source):
    """
    Returns packages using shell script (apt, snap, flatpack) as a list
    """

    result = subprocess.run([f'./scripts/{source}.sh'], stdout=subprocess.PIPE)
    return str(result.stdout).replace("b'", "").replace("'", "")


def get_apt_packages():
    """
    Returns apt packages using shell script as a list
    """

    list = get_packages("apt").split("\\n")
    list.remove("Listing...")
    list.remove('')
    return list


def get_apt_repos():
    """
    Returns  apt repositories using shell script as a list
    """

    apt_repos = get_packages("apt_repos").split("\\n")
    return apt_repos


def get_gnome_extensions():
    """
    Returns gnome extensions using shell script as a list
    """

    extensions = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    extensions = str(extensions.stdout).replace("b'", "").replace("'", "")
    list = extensions.split("\\n")
    list.remove('')
    return list


def get_flatpak_packages():
    """
    Returns flatpak packages using shell script as a list
    """

    list = get_packages("flatpak").split("\\n")
    list.remove('')
    return list


def get_snap_packages():
    """
    Returns snap packages using shell script as a list
    """

    list = get_packages("snap").split("\\n")
    list.remove('')
    return list


def get_sources_keys():
    """
    Returns apt source keys as a list of [path, bytes]
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
    Returns ssh keys as a list of [path, contents]
    """

    files = []
    sources = []
    w = os.walk(os.path.expanduser('~')+"/.ssh")
    for root, dirs, files_list in w:
        files = files_list


    for i in range(0, len(files)-1):
        file = files[i]
        result = subprocess.run([f'./scripts/ssh.sh', file], stdout=subprocess.PIPE).stdout
        sources.append([])
        sources[i].append(file)
        sources[i].append(str(result)) 

    for source in sources:
        source[0] = "~/.ssh/" + source[0]

    return sources


def get_shell_themes():
    """
    Returns the shell themes as bytes of a zip file
    """

    data = b""
    name = os.path.expanduser('~')+"/shell-themes-cvf"
    shutil.make_archive(name, 'zip', "/usr/share/themes")
    with open(name, "rb") as file:
        data = file.read()

    os.remove(name)
    return data


def get_dconf():
    """
    Returns the dconf file as bytes
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
    Returns all the git repos that have a remote, starting from a specific path as a list of
    [path, remote-url].
    The method excludes git submodules.
    """

    path = path or "$HOME"  # I dont know if this works

    def run_shell_command(command):
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return ""

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
