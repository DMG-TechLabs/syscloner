from constants import GNOME, UBUNTU
import get_methods
import file_builder

builder = file_builder.FileBuilder()

# builder.set_apt_pkgs(get_methods.get_apt_packages())

builder.build("kdesp73", UBUNTU, GNOME)
