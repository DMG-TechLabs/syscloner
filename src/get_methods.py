from pdb import run
import shutil
import os
import subprocess


def get_bytes(file):
    temp = ""
    with open(file, "rb") as filename:
        temp = filename.read() 
        filename.close()
    return temp


def get_packages(source):
    result = subprocess.run([f'./scripts/{source}.sh'], stdout=subprocess.PIPE)
    return str(result.stdout).replace("b'", "").replace("'", "")


def get_apt_packages():
    list = get_packages("apt").split("\\n")
    list.remove("Listing...")
    list.remove('')
    return list


def get_apt_repos():
    apt_repos = get_packages("apt_repos").split("\\n")
    return apt_repos


def get_gnome_extensions():
    extensions = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    extensions = str(extensions.stdout).replace("b'", "").replace("'", "")
    list = extensions.split("\\n")
    list.remove('')
    return list


def get_flatpak_packages():
    list = get_packages("flatpak").split("\\n")
    list.remove('')
    return list


def get_snap_packages():
    list = get_packages("snap").split("\\n")
    list.remove('')
    return list


def get_sources_keys():
    files = []
    sources = []
    w = os.walk("/etc/apt")
    for root, dirs, files_list in w:
        # print(files_list)
        for file in files_list:
            if file.endswith(".gpg") or file.endswith(".asc"):
                files.append(os.path.join(root, file))

    # print(files)

    for i in range(0,len(files)-1):
        file = files[i]
        with open(file, "rb") as filename:
            sources.append([])
            sources[i].append(file)
            sources[i].append(filename.read()) 
            filename.close()
    return sources


def get_ssh_keys():
    files = []
    sources = []
    w = os.walk(os.path.expanduser('~')+"/.ssh")
    for root, dirs, files_list in w:
        # print(files_list)
        files = files_list

    for i in range(0, len(files)-1):
        file = files[i]
        result = subprocess.run([f'./scripts/ssh.sh', file], stdout=subprocess.PIPE).stdout
        sources.append([])
        sources[i].append(file)
        sources[i].append(str(result)) 
    return sources

def get_shell_themes():
    data = b""
    name = os.path.expanduser('~')+"/shell-themes-cvf"
    shutil.make_archive(name, 'zip', "/usr/share/themes")
    with open(name, "rb") as file:
        data = file.read()
    return data

def get_dconf():
    return get_bytes(os.path.expanduser('~')+"/.config/dconf/user")

def get_git_repos(path):
    num_of_repos = subprocess.run([f'./scripts/num_of_repos.sh', str(path)], stdout=subprocess.PIPE)
    num_of_repos = int(num_of_repos.stdout)

    git_repos = [[""]*2]*num_of_repos

    for i in range(0, num_of_repos):
        temp_array = [""]*2
        git_repo_path = subprocess.run([f'./scripts/git_repos_paths.sh', str(i+1), str(path)], stdout=subprocess.PIPE)
        temp_array[0] = str(git_repo_path.stdout).replace("b'", "").replace("\\n'", "")
        # print(temp_array[0])
        
        git_repo_url = subprocess.run([f'./scripts/git_repos.sh', temp_array[0]], stdout=subprocess.PIPE)
        temp_array[1] = str(git_repo_url.stdout).replace("b'", "").replace("\\n'", "")
        # print(result)
        git_repos[i] = temp_array
        # print("(" + git_repos[i][0] + ", "+ git_repos[i][1] + ")")
    return git_repos
