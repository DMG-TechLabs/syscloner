from os import walk
import os
import subprocess


def install_packages(source, packages):
    """
    Installs packages using `sudo [package-manager] install -y`

    Parameters
    ----------
    source: string
        package manager (apt, snap, flatpak)
    packages: list
        the list of package names
    """

    for package in packages:
        subprocess.run(['sudo', source, 'install', package, '-y'])


def install_flatpak_packages(packages):
    """
    Installs flatpak packages

    Parameters
    ----------
    packages: list
        the list of flatpak packages
    """

    install_packages("flatpak", packages)


def install_snap_packages(packages):
    """
    Installs snap packages

    Parameters
    ----------
    packages: list
        the list of snap packages
    """

    install_packages("snap", packages)


def install_apt_packages(packages):
    """
    Installs apt packages

    Parameters
    ----------
    packages: list
        the list of apt packages
    """

    install_packages("apt", packages)


def install_gnome_extensions(extensions):
    """
    Installs gnome extensions

    Parameters
    ----------
    extensions: list
        the list of gnome extensions
    """

    install_packages("gnome-extensions", extensions)


def install_files_from_bytes(files, write_mode):
    """
    Write files multiple files specifying the write mode

    Parameters
    ----------
    files: list
        list of files as [path, contents]
    write_mode: str
        the write mode (i.e. 'w', 'wb')
    """

    for file in files:
        with open(file[0], write_mode) as filename:
            filename.write(file[1])
            filename.close()


def install_git_repos(repos):
    """
    Clones the git repos at their specified path

    Parameters
    ----------
    repos: list
        the list of repos as [path, remote-url]
    """

    for repo in repos:
        subprocess.run([f'git clone {repo[1]} {repo[0]}'], stdout=subprocess.PIPE)
