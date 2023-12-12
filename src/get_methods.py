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

# def get_ssh_keys():

def get_flatpak_packages():
    return get_packages("flatpak")


def get_snap_packages():
    return get_packages("snap")

def get_apt_repos():
    return get_packages("apt_repos")
