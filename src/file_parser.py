import constants
import os
from logger import erro, info, debu

from metadata import is_metadata, metadata, parse_metadata


class FileParser:
    """
    Class that parses `.cvf` files

    After parsing the values are stores inside the parser object for the
    installer to use
    """

    # Private (i hate this)
    __index = 0
    __lines = []

    file_metadata = dict()

    system_settings = b""
    shell_themes = b""
    apt_packages = []
    snap_packages = []
    flatpak_packages = []
    gnome_extensions = []
    apt_repositories = list()
    repository_keys = list()    # 2d array
    ssh = list()  # 2d array
    git_repos = list()  # 2d array

    def __init__(self, file):
        """
        Constructor

        Parameters
        ----------
        file: string
            path of cvf file to parse
        """

        filename, extension = os.path.splitext(file)
        if extension != '.cvf':
            raise ValueError(f"File '{file}' is not cvf")

        self.file = open(file, "r")
        try:
            self.__lines = self.file.read().split("\n")
        except FileNotFoundError:
            erro("File not found. Aborting parsing...\n")

    def advance(self):
        """
        Proceed by one line
        """

        self.__index += 1

    def skip_blank_lines(self):
        while self.__index+1 < self.__lines.__len__() and (self.__lines[self.__index] == "\n" or self.__lines[self.__index] == "" or self.__lines[self.__index].__len__()):
            self.advance()

    def parse(self):
        """
        Starts the cvf file parsing operation
        """
        
        while self.__index < self.__lines.__len__():
            if is_metadata(self.__lines[self.__index]):
                pair = parse_metadata(self.__lines[self.__index])
                if pair[0] == 'distro' or pair[0] == 'gui':
                    self.file_metadata[pair[0]] = pair[1].lower()
                else:
                    self.file_metadata[pair[0]] = pair[1]
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
                self.apt_repositories = self.parse_file_contents()
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
                self.ssh = self.parse_file_contents()
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

    def parse_file_contents(self):
        lst = list()
        while self.__lines[self.__index] != constants.SEPARATOR:
            self.advance()
            file = []
            file.append(self.__lines[self.__index])  # Path
            contents = ""
            while self.__lines[self.__index].__len__() != 0 and self.__lines[self.__index] != constants.SEPARATOR:
                self.advance()
                contents += self.__lines[self.__index] + "\n"
            file.append(contents)
            lst.append(file)

        def remove_items(test_list, item):
            res = [i for i in test_list if i != item]
            return res

        # Remove last false elements
        lst = remove_items(lst, ['', ''])
        lst = remove_items(lst, [constants.SEPARATOR, ''])
        return lst


if __name__ == "__main__":
    parser = FileParser('./test_ub_gn.cvf')
    parser.parse()

    for pair in parser.repository_keys:
        print(pair[0])
        print(pair[1])
        print('\n')
