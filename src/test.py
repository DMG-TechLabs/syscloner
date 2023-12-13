from constants import GNOME, UBUNTU
from file_builder import FileBuilder
import get_methods

builder = FileBuilder()
builder.include_all()

builder.build("test", UBUNTU, GNOME)
