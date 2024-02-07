import argparse
from constants import GNOME, UBUNTU
from file_builder import FileBuilder
from file_parser import FileParser
from installer import FileInstaller



def main():
    builder = FileBuilder()
    args_parser = argparse.ArgumentParser(
            prog='system-cloner',
            description='Clones your system',
            epilog='Made by DMG-TechLabs')

    args_parser.add_argument('action', choices=['backup', 'restore'])
    args_parser.add_argument('name')

    args_parser.add_argument("--system", required=False, action='count')
    args_parser.add_argument("--apt", required=False, action='count')
    args_parser.add_argument("--snap", required=False, action='count')
    args_parser.add_argument("--flatpak", required=False, action='count')
    args_parser.add_argument("--themes", required=False, action='count')
    args_parser.add_argument("--exts", required=False, action='count')
    args_parser.add_argument("--keys", required=False, action='count')
    args_parser.add_argument("--ssh", required=False, action='count')
    args_parser.add_argument("--all", required=False, action='count')

    args = args_parser.parse_args()
    print(args)

    if args.action == 'restore':
        parser = FileParser(args.name)
        parser.parse()
        installer = FileInstaller(parser)
        installer.install(parser)
        exit(0)

    if args.all:
        builder.include_all()
        builder.build(args.name, UBUNTU, GNOME) # Check distro and shell
        exit(0)

    if args.system:
        builder.include_system_settings()

    if args.apt:
        builder.include_apt_packages()

    if args.snap:
        builder.include_snap_packages()

    if args.flatpak:
        builder.include_flatpak_packages()

    if args.themes:
        builder.include_shell_themes()

    if args.exts:
        builder.include_gnome_extensions()

    if args.keys:
        builder.include_repository_keys()

    if args.ssh:
        builder.include_ssh()

    builder.build(args.name, UBUNTU, GNOME)


if __name__ == "__main__":
    main()
