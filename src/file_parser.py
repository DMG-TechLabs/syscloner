import constants
from logging import erro, info


class FileParser:
    """Class that parses `.cvf` files
    After parsing the values are stores inside the parser object for the installer to use
    """
    
    # Private (i hate this)
    __index = 0
    __lines = []

    system_settings = b""
    shell_themes = b""
    apt_packages = []
    snap_packages = []
    flatpak_packages = []
    gnome_extensions = []
    apt_repositories = ""
    repository_keys = list()    # 2d array
    ssh = list()  # 2d array
    git_repos = list()  # 2d array

    def __init__(self, file):
        self.file = open(file, "r")
        try:
            self.__lines = self.file.read().split("\n")
        except FileNotFoundError:
            erro("File not found. Aborting parsing...\n")

    def advance(self):
        self.__index += 1

    def parse(self):
        while self.__index < self.__lines.__len__():
            # TODO: parse metadata
            if self.__lines[self.__index] == constants.SYSTEM_SETTINGS:
                self.advance()
                self.system_settings = self.__lines[self.__index]
                self.advance()  # Consume closing tag
            elif self.__lines[self.__index] == constants.SHELL_THEMES:
                self.advance()
                self.shell_themes = self.__lines[self.__index]
                self.advance()  # Consume closing tag
            elif self.__lines[self.__index] == constants.APT_PACKAGES:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    self.apt_packages.append(self.__lines[self.__index])
                    self.advance()
            elif self.__lines[self.__index] == constants.SNAP_PACKAGES:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    self.snap_packages.append(self.__lines[self.__index])
                    self.advance()
            elif self.__lines[self.__index] == constants.FLATPAK_PACKAGES:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    self.flatpak_packages.append(self.__lines[self.__index])
                    self.advance()
            elif self.__lines[self.__index] == constants.GNOME_EXTENSIONS:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    self.gnome_extensions.append(self.__lines[self.__index])
                    self.advance()
            elif self.__lines[self.__index] == constants.APT_REPOSITORIES:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    self.apt_repositories += self.__lines[self.__index] + "\n"
                    self.advance()
            elif self.__lines[self.__index] == constants.REPOSITORY_KEYS:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    key_path = self.__lines[self.__index]
                    self.advance()
                    key_bytes = self.__lines[self.__index]
                    self.repository_keys.append([key_path, key_bytes])
                    self.advance()

                    if self.__lines[self.__index] == "":
                        self.advance()  # Consume blank line
            elif self.__lines[self.__index] == constants.SSH:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    key_path = self.__lines[self.__index]
                    self.advance()
                    key_bytes = self.__lines[self.__index]
                    self.ssh.append([key_path, key_bytes])
                    self.advance()

                    if self.__lines[self.__index] == "":
                        self.advance()  # Consume blank line
            elif self.__lines[self.__index] == constants.GIT_REPOSITORIES:
                self.advance()
                while self.__lines[self.__index] != constants.SEPARATOR:
                    repo_path = self.__lines[self.__index]
                    self.advance()
                    repo_url = self.__lines[self.__index]
                    self.git_repos.append([repo_path, repo_url])
                    self.advance()

                    if self.__lines[self.__index] == "":
                        self.advance()  # Consume blank line
            self.advance()


print(FileParser.__doc__)
