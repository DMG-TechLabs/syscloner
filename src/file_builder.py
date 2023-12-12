from constants import APT_PACKAGES, EXTENSION, FLATPAK_PACKAGES, GNOME_EXTENSIONS, SEPARATOR, SHELL_THEMES, SNAP_PACKAGES, SYSTEM_SETTINGS
from metadata import get_os, get_distro, metadata
import get_methods

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

    def build(self, name, os, distro) -> None:
        filename = f"{name}{os}{distro}.{EXTENSION}"

        contents = ""
        # Metadata
        contents += metadata("name", name) + "\n"
        contents += metadata("os", get_os(os)) + "\n"
        contents += metadata("distro", get_distro(distro)) + "\n"

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
        for package in get_methods.get_gnome_extensions():
            contents += package + "\n"
        contents += SEPARATOR + "\n\n\n"

        contents += SHELL_THEMES + "\n"
        for package in get_methods.get_gnome_extensions():
            contents += package + "\n"
        contents += SEPARATOR + "\n\n\n"
        file = open(filename, "w")
        file.write(contents)
        file.close()

        print("File written successfully")
