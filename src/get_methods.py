import subprocess

def get_apt_packages():
    result = subprocess.run(['apt', 'list', '--installed'], stdout=subprocess.PIPE)
    packages = str(result.stdout).replace("\'", "").strip()
    return packages.split("\\n")

def get_gnome_extensions():
    result = subprocess.run(['gnome-extensions', 'list'], stdout=subprocess.PIPE)
    result = str(result.stdout).replace("b'", "")
    return result.split("\\n")
