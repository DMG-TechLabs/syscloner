import shutil
from file_parser import FileParser
import install_methods
from logging import succ, warn


class Installer:
    """
    The installer object takes as a parameter a parser object and after some configuring installs everything on the computer
    """

    system_settings_included = False
    apt_packages_included = False
    snap_packages_included = False
    flatpak_packages_included = False
    gnome_extensions_included = False
    repository_keys_included = False
    shell_themes_included = False
    apt_repositories_included = False
    git_repositories_included = False
    ssh_included = False

    def __init__(self, parser: FileParser) -> None:
        self.parser = parser

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

    def include_git_repositories(self):
        self.git_repositories_included = True

    def include_ssh(self):
        self.ssh_included = True

    def include_all(self):
        self.include_apt_repositories()
        self.include_git_repositories()
        self.include_repository_keys()
        self.include_ssh()
        self.include_apt_packages()
        self.include_system_settings()
        self.include_shell_themes()
        self.include_snap_packages()
        self.include_gnome_extensions()
        self.include_flatpak_packages()

    def install(self):
        """
        The method that starts the installation
        """

        self.__install_apt_packages()
        self.__install_snap_packages()
        self.__install_flatpak_packages()
        self.__install_gnome_extensions()
        self.__install_system_settings()
        self.__install_shell_themes()
        self.__install_apt_repos()
        self.__install_repo_keys()
        self.__install_ssh()
        self.__install_git_repos()

    def __install_apt_packages(self):
        if self.apt_packages_included and self.parser.apt_packages != []:
            install_methods.install_apt_packages(self.parser.apt_packages)

    def __install_snap_packages(self):
        if self.snap_packages_included and self.parser.snap_packages != []:
            install_methods.install_snap_packages(self.parser.snap_packages)

    def __install_flatpak_packages(self):
        if self.flatpak_packages_included and self.parser.flatpak_packages != []:
            install_methods.install_flatpak_packages(self.parser.flatpak_packages)

    def __install_gnome_extensions(self):
        if self.gnome_extensions_included and self.parser.gnome_extensions != []:
            install_methods.install_gnome_extensions(self.parser.gnome_extensions)

    def __install_system_settings(self):
        if self.system_settings_included and self.parser.system_settings != b"":
            install_methods.install_files_from_bytes(list(['~/.config/dconf/user', self.parser.system_settings]), "wb")

    def __install_shell_themes(self):
        if self.shell_themes_included and self.parser.shell_themes != b"":
            zip = '/usr/share/themes/shell-themes.zip'
            install_methods.install_files_from_bytes(list([zip, self.parser.shell_themes]), "wb")
            shutil.unpack_archive(zip)

    def __install_apt_repos(self):
        # TODO: apt repos
        if self.apt_repositories_included:
            warn("Installation not implemented yet.")

    def __install_repo_keys(self):
        if self.repository_keys_included and self.parser.repository_keys.__len__() != 0:
            install_methods.install_files_from_bytes(self.parser.repository_keys, "wb")

    def __install_ssh(self):
        if self.ssh_included and self.parser.ssh.__len__() != 0:
            install_methods.install_files_from_bytes(self.parser.ssh, "wb")

    def __install_git_repos(self):
        if self.git_repositories_included and self.parser.git_repos.__len__() != 0:
            install_methods.install_git_repos(self.parser.git_repos)
