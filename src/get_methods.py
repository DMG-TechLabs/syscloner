import glob
import os
import subprocess


def get_packages(source):
    result = subprocess.run([f'./scripts/{source}.sh'], stdout=subprocess.PIPE)
    return result


def get_apt_packages():
    return get_packages("apt")


def get_gnome_extensions():
    extensions = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    extensions = str(extensions.stdout).replace("b'", "").replace("'", "")
    return extensions.split("\\n")


def get_flatpak_packages():
    return get_packages("flatpak")


def get_snap_packages():
    return get_packages("snap")

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

