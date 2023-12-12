from constants import APT_PACKAGES, APT_REPOSITORIES, CONFIGS, EXTENSION, FLATPAK_PACKAGES, GNOME_EXTENSIONS, REPOSITORY_KEYS, SEPARATOR, SHELL_THEMES, SSH, SNAP_PACKAGES, SYSTEM_SETTINGS
from metadata import get_os, get_distro, metadata
import get_methods
from datetime import datetime


class FileBuilder:
    def __init__(self,
                 system_settings=None,
                 apt_pkgs=None,
                 snap_pkgs=None,
                 flatpak_pkgs=None,
                 apt_repos=None,
                 repo_keys=None,
                 gnome_exts=None,
                 shell_themes=None,
                 ssh_keys=None,
                 configs=None
                 ):
        self.system_settings = system_settings
        self.apt_pkgs = apt_pkgs
        self.snap_pkgs = snap_pkgs
        self.flatpak_pkgs = flatpak_pkgs
        self.apt_repos = apt_repos
        self.repo_keys = repo_keys
        self.gnome_exts = gnome_exts
        self.shell_themes = shell_themes
        self.ssh_keys = ssh_keys
        self.configs = configs

    def set_system_settings(self, system_settings):
        self.system_settings = system_settings

    def set_apt_pkgs(self, apt_pkgs):
        self.apt_pkgs = apt_pkgs

    def set_snap_pkgs(self, snap_pkgs):
        self.snap_pkgs = snap_pkgs

    def set_flatpak_pkgs(self, flatpak_pkgs):
        self.flatpak_pkgs = flatpak_pkgs

    def set_apt_repos(self, apt_repos):
        self.apt_repos = apt_repos

    def set_repo_keys(self, repo_keys):
        self.repo_keys = repo_keys

    def set_gnome_exts(self, gnome_exts):
        self.gnome_exts = gnome_exts

    def set_shell_themes(self, shell_themes):
        self.shell_themes = shell_themes

    def set_ssh_keys(self, ssh_keys):
        self.ssh_keys = ssh_keys

    def set_configs(self, configs):
        self.configs = configs

    def build(self, name, distro, shell) -> None:
        filename = f"{name}{distro}{shell}.{EXTENSION}"

        now = datetime.now()
        contents = ""
        # Metadata
        contents += metadata("name", name) + "\n"
        contents += metadata("date", now.strftime("%d/%m/%Y %H:%M:%S")) + "\n"
        contents += metadata("distro", get_os(distro)) + "\n"
        contents += metadata("shell", get_distro(shell)) + "\n"

        contents += "\n\n\n"

        contents += SYSTEM_SETTINGS + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += APT_PACKAGES + "\n"
        for package in get_methods.get_apt_packages():
            contents += package + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += SNAP_PACKAGES + "\n"
        for package in get_methods.get_snap_packages():
            contents += package + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += FLATPAK_PACKAGES + "\n"
        for package in get_methods.get_flatpak_packages():
            contents += package + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += GNOME_EXTENSIONS + "\n"
        for extension in get_methods.get_gnome_extensions():
            contents += extension + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += REPOSITORY_KEYS + "\n"
        for pair in get_methods.get_sources_keys():
            contents += pair[0] + "\n"
            contents += str(pair[1]) + "\n\n"
        contents += SEPARATOR + "\n\n\n"

        contents += SHELL_THEMES + "\n"
        try:
            contents += str(get_methods.get_shell_themes())
        except FileNotFoundError:
            contents += "Error\n"
            print("Error with shell themes")
        contents += SEPARATOR + "\n\n\n"

        contents += APT_REPOSITORIES + "\n"
        for repo in get_methods.get_apt_repos():
            contents += repo + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += SSH + "\n"
        try:
            for pair in get_methods.get_ssh_keys():
                contents += pair[0] + "\n"
                contents += pair[1] + "\n\n"
        except FileNotFoundError:
            print("Error with ssh")
            contents += "Error\n"
        contents += SEPARATOR + "\n\n\n"

        contents += CONFIGS + "\n"
        contents += SEPARATOR + "\n\n\n"

        file = open(filename, "w")
        file.write(contents)
        file.close()

        print("File written successfully")
