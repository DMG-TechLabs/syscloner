import subprocess


def get_flatpak_packages():
    result = subprocess.run(['flatpak', 'list'], stdout=subprocess.PIPE)
    packages = str(result.stdout).replace("\'", "").strip()
    return packages.split("\\n")


def install_flatpak_packages(packages):
    for line in packages:
        line = line.split(",")[0].split("/")[0]
        subprocess.run(['sudo', 'apt', 'install', line])
        
        
if __name__ == "__main__":
    result = subprocess.run(["flatpak", "list"], stdout=subprocess.PIPE)
    result = subprocess.run([ 'tr', "--squeeze-repeats", '"\t"', result.stdout], stdout=subprocess.PIPE)
    result = subprocess.run(['cut', "-d$'\t'", '-f2' , result.stdout], stdout=subprocess.PIPE)
    for i in str(result.stdout).split("\\n"):
        print(i)
        
