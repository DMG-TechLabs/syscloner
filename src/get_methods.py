import shutil
import os
import subprocess

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

    # print(files)

    for i in range(0, len(files)-1):
        file = files[i]
        with open(file, "r") as filename:
            sources.append([])
            sources[i].append(file)
            sources[i].append(filename.read()) 
            filename.close()
    return sources

def get_shell_themes():
    data = b""
    name = os.path.expanduser('~')+"/shell-themes-cvf"
    shutil.make_archive(name, 'zip', "/usr/share/themes")
    with open(name, "rb") as file:
        data = file.read()
    return data
