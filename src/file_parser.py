import constants


class FileParser:
    index = 0
    lines = []

    system_settings = b""
    apt_packages = []
    snap_packages = []
    flatpak_packages = []
    gnome_extensions = []
    apt_repositories = ""
    repository_keys = list()    # 2d array
    shell_themes = b""
    ssh = list()  # 2d array
    configs = list()    # 2d array

    def __init__(self, file):
        self.file = open(file, "r")
        try: 
            self.lines = self.file.read().split("\n")
        except FileNotFoundError:
            print("File not found. Aborting parsing...\n")

    def advance(self):
        self.index += 1

    def parse(self):
        while self.index < self.lines.__len__():
            if self.lines[self.index] == constants.SYSTEM_SETTINGS:
                self.advance()
                self.system_settings = self.lines[self.index]
                self.advance()  # Consume closing tag
            elif self.lines[self.index] == constants.SHELL_THEMES:
                self.advance()
                self.shell_themes = self.lines[self.index]
                self.advance()  # Consume closing tag
            elif self.lines[self.index] == constants.APT_PACKAGES:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    self.apt_packages.append(self.lines[self.index])
                    self.advance()
            elif self.lines[self.index] == constants.SNAP_PACKAGES:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    self.snap_packages.append(self.lines[self.index])
                    self.advance()
            elif self.lines[self.index] == constants.FLATPAK_PACKAGES:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    self.flatpak_packages.append(self.lines[self.index])
                    self.advance()
            elif self.lines[self.index] == constants.GNOME_EXTENSIONS:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    self.gnome_extensions.append(self.lines[self.index])
                    self.advance()
            elif self.lines[self.index] == constants.APT_REPOSITORIES:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    self.apt_repositories += self.lines[self.index] + "\n"
                    self.advance()
            elif self.lines[self.index] == constants.REPOSITORY_KEYS:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    key_path = self.lines[self.index]
                    self.advance()
                    key_bytes = self.lines[self.index]
                    self.repository_keys.append([key_path, key_bytes])
                    self.advance()

                    if self.lines[self.index] == "":
                        self.advance()  # Consume blank line
            elif self.lines[self.index] == constants.SSH:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    key_path = self.lines[self.index]
                    self.advance()
                    key_bytes = self.lines[self.index]
                    self.ssh.append([key_path, key_bytes])
                    self.advance()

                    if self.lines[self.index] == "":
                        self.advance()  # Consume blank line
            elif self.lines[self.index] == constants.CONFIGS:
                self.advance()
                while self.lines[self.index] != constants.SEPARATOR:
                    key_path = self.lines[self.index]
                    self.advance()
                    key_bytes = self.lines[self.index]
                    self.configs.append([key_path, key_bytes])
                    self.advance()

                    if self.lines[self.index] == "":
                        self.advance()  # Consume blank line
            self.advance()
