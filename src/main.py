from constants import GNOME, UBUNTU
import get_methods
import file_builder


def main():
    builder = file_builder.FileBuilder()
    builder.include_system_settings()
    builder.include_apt_packages()
    builder.include_ssh()
    builder.include_repository_keys()
    builder.build("kdesp73", UBUNTU, GNOME)





if __name__ == "__main__":
    main()
