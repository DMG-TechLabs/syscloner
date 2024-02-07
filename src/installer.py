import shutil
from file_parser import FileParser
import install_methods


class Installer:
    def __init__(self, parser: FileParser) -> None:
        self.parser = parser

    def install(self):
        if self.parser.apt_packages != []:
            install_methods.install_apt_packages(self.parser.apt_packages)

        if self.parser.snap_packages != []:
            install_methods.install_snap_packages(self.parser.snap_packages)

        if self.parser.flatpak_packages != []:
            install_methods.install_flatpak_packages(self.parser.flatpak_packages)

        if self.parser.gnome_extensions != []:
            install_methods.install_gnome_extensions(self.parser.gnome_extensions)

        if self.parser.system_settings != b"":
            install_methods.install_files_from_bytes(list(['~/.config/dconf/user', self.parser.system_settings]), "wb")

        if self.parser.shell_themes != b"":
            zip = '/usr/share/themes/shell-themes.zip'
            install_methods.install_files_from_bytes(list([zip, self.parser.shell_themes]), "wb")
            shutil.unpack_archive(zip)

        # TODO: apt repos

        if self.parser.repository_keys.__len__() != 0:
            install_methods.install_files_from_bytes(self.parser.repository_keys, "wb")

        if self.parser.ssh.__len__() != 0:
            install_methods.install_files_from_bytes(self.parser.ssh, "wb")

        if self.parser.configs.__len__() != 0:
            install_methods.install_files_from_bytes(self.parser.configs, "wb")
