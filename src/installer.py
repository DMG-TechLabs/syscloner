import install_methods


class Installer:
    def __init__(self, parser) -> None:
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

        # if self.parser.system_settings != b"":
        #     # TODO: install_system_settings()
        #
        # if self.parser.shell_themes != b"":
        #     # TODO: install_shell_themes()
        #
        # if self.apt_repositories != "":
        #     # TODO: install_apt_repository()


