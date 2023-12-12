import subprocess


def get_packages(source):
    result = subprocess.run([f'./scripts/{source}.sh'], stdout=subprocess.PIPE)
    return str(result.stdout).replace("b'", "").replace("'", "")


def get_apt_packages():
    list = get_packages("apt").split("\\n")
    list.remove("Listing...")
    return list


def get_gnome_extensions():
    extensions = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    extensions = str(extensions.stdout).replace("b'", "").replace("'", "")
    return extensions.split("\\n")


def get_flatpak_packages():
    list = get_packages("flatpak").split("\\n")
    list.remove('')
    return list


def get_snap_packages():
    list = get_packages("snap").split("\\n")
    list.remove('')
    return list
