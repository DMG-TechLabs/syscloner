import subprocess


def get_packages(source):
    result = subprocess.run([f'./scripts/{source}.sh'], stdout=subprocess.PIPE)
    return result


def get_apt_packages():
    result = subprocess.run(['sudo', './scripts/apt.sh'], stdout=subprocess.PIPE)
    return result.stdout


def get_gnome_extensions():
    extensions = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    extensions = str(extensions.stdout).replace("b'", "").replace("'", "")
    return extensions.split("\\n")


def get_flatpak_packages():
    result = subprocess.run(['./scripts/flatpak.sh'], stdout=subprocess.PIPE)
    return result.stdout


def get_snap_packages():
    result = subprocess.run(['./scripts/snap.sh'], stdout=subprocess.PIPE)
    return result.stdout
