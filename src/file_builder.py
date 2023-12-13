import constants
from metadata import get_os, get_distro, metadata
import get_methods
from datetime import datetime


class FileBuilder:
    system_settings_included = False
    apt_packages_included = False
    snap_packages_included = False
    flatpak_packages_included = False
    gnome_extensions_included = False
    repository_keys_included = False
    shell_themes_included = False
    apt_repositories_included = False
    ssh_included = False
    configs_included = False

    def __init__(self) -> None:
        pass

    def include_system_settings(self):
        self.system_settings_included = True

    def include_apt_packages(self):
        self.apt_packages_included = True

    def include_snap_packages(self):
        self.snap_packages_included = True

    def include_flatpak_packages(self):
        self.flatpak_packages_included = True

    def include_gnome_extensions(self):
        self.gnome_extensions_included = True

    def include_repository_keys(self):
        self.repository_keys_included = True

    def include_shell_themes(self):
        self.shell_themes_included = True

    def include_apt_repositories(self):
        self.apt_repositories_included = True

    def include_ssh(self):
        self.ssh_included = True

    def include_configs(self):
        self.configs_included = True

    def build(self, name, distro, shell) -> None:
        filename = f"{name}{distro}{shell}.{constants.EXTENSION}"

        now = datetime.now()

        # Metadata
        contents = metadata("name", name) + "\n"
        contents += metadata("date", now.strftime("%d/%m/%Y %H:%M:%S")) + "\n"
        contents += metadata("distro", get_os(distro)) + "\n"
        contents += metadata("shell", get_distro(shell)) + "\n"

        contents += "\n\n\n"

        contents += system_settings() if self.system_settings_included else ""
        contents += apt_packages() if self.apt_packages_included else ""
        contents += snap_packages() if self.snap_packages_included else ""
        contents += flatpak_packages() if self.flatpak_packages_included else ""
        contents += gnome_extensions() if self.gnome_extensions_included else ""
        contents += repository_keys() if self.repository_keys_included else ""
        contents += shell_themes() if self.shell_themes_included else ""
        contents += apt_repositories() if self.apt_repositories_included else ""
        contents += ssh() if self.ssh_included else ""
        contents += configs() if self.configs_included else ""

        file = open(filename, "w")
        file.write(contents)
        file.close()

        print("File written successfully")


def system_settings():
    contents = constants.SYSTEM_SETTINGS + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def apt_packages():
    contents = constants.APT_PACKAGES + "\n"
    for package in get_methods.get_apt_packages():
        contents += package + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def snap_packages():
    contents = constants.SNAP_PACKAGES + "\n"
    for package in get_methods.get_snap_packages():
        contents += package + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def flatpak_packages():
    contents = constants.FLATPAK_PACKAGES + "\n"
    for package in get_methods.get_flatpak_packages():
        contents += package + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def gnome_extensions():
    contents = constants.GNOME_EXTENSIONS + "\n"
    for extension in get_methods.get_gnome_extensions():
        contents += extension + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def repository_keys():
    contents = constants.REPOSITORY_KEYS + "\n"
    for pair in get_methods.get_sources_keys():
        contents += pair[0] + "\n"
        contents += str(pair[1]) + "\n\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def shell_themes():
    contents = constants.SHELL_THEMES + "\n"
    try:
        contents += str(get_methods.get_shell_themes())
    except FileNotFoundError:
        contents += "Error\n"
        print("Error with shell themes")
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def apt_repositories():
    contents = constants.APT_REPOSITORIES + "\n"
    for repo in get_methods.get_apt_repos():
        contents += repo + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def ssh():
    contents = constants.SSH + "\n"
    try:
        for pair in get_methods.get_ssh_keys():
            contents += pair[0] + "\n"
            contents += pair[1] + "\n\n"
    except FileNotFoundError:
        print("Error with ssh")
        contents += "Error\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents


def configs():
    contents = constants.CONFIGS + "\n"
    contents += constants.SEPARATOR + "\n\n\n"
    return contents
