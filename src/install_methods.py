import subprocess

def install_apt_packages(packages):
    for line in packages:
        line = line.split(",")[0].split("/")[0]
        subprocess.run(['sudo', 'apt', 'install', line])

# NOT WORKING YET
# def install_gnome_extensions(extensions):
#     for line in extensions:
#         line = line.split()
#         subprocess.run(["gnome-extensions", "install", line])
