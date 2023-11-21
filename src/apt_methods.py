import subprocess


def get_apt_packages():
    result = subprocess.run(['apt', 'list', '--installed'], stdout=subprocess.PIPE)
    packages = str(result.stdout).replace("\'", "").strip()
    return packages.split("\\n")


def install_apt_packages(packages):
    for line in packages:
        line = line.split(",")[0].split("/")[0]
        subprocess.run(['sudo', 'apt', 'install', line])
