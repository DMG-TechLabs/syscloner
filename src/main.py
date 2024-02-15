import argparse
from sys import version
from constants import GNOME, UBUNTU
from file_builder import FileBuilder
from file_parser import FileParser
from installer import Installer


def restore(args):
    parser = FileParser(args.name)
    parser.parse()
    installer = Installer(parser)

    if args.all is not None:
        installer.include_all()
        installer.install()
        exit(0)

    if args.system is not None:
        installer.include_system_settings()

    if args.apt is not None:
        installer.include_apt_packages()

    if args.snap is not None:
        installer.include_snap_packages()

    if args.flatpak is not None:
        installer.include_flatpak_packages()

    if args.themes is not None:
        installer.include_shell_themes()

    if args.exts is not None:
        installer.include_gnome_extensions()

    if args.keys is not None:
        installer.include_repository_keys()

    if args.ssh is not None:
        installer.include_ssh()

    if args.git_repos is not None:
        installer.include_git_repositories()

    installer.install()


def backup(args):
    builder = FileBuilder()
    if args.all is not None:
        builder.include_all(args.git_repos)
        builder.build(args.filename, UBUNTU, GNOME)  # TODO: Check distro and shell
        return

    if args.system is not None:
        builder.include_system_settings()

    if args.apt is not None:
        builder.include_apt_packages()

    if args.snap is not None:
        builder.include_snap_packages()

    if args.flatpak is not None:
        builder.include_flatpak_packages()

    if args.themes is not None:
        builder.include_shell_themes()

    if args.exts is not None:
        builder.include_gnome_extensions()

    if args.keys is not None:
        builder.include_repository_keys()

    if args.ssh is not None:
        builder.include_ssh()

    if args.git_repos is not None:
        builder.include_git_repositories(args.git_repos)

    builder.build(args.filename, UBUNTU, GNOME)


def main():
    args_parser = argparse.ArgumentParser(
            prog='system-cloner',
            description='Clones your system',
            epilog='Made by DMG-TechLabs')

    args_parser.add_argument('action', choices=['backup', 'restore'])
    args_parser.add_argument('filename')

    args_parser.add_argument(
            '--system',
            required=False,
            action='count',
            help='include system settings')

    args_parser.add_argument(
            '--apt',
            required=False,
            action='count',
            help='include apt packages')

    args_parser.add_argument(
            '--snap',
            required=False,
            action='count',
            help='include snap packages')

    args_parser.add_argument(
            '--flatpak',
            required=False,
            action='count',
            help='include flatpak packages')

    args_parser.add_argument(
            '--themes',
            required=False,
            action='count',
            help='include shell themes')

    args_parser.add_argument(
            '--exts',
            required=False,
            action='count',
            help='include shell extensions')

    args_parser.add_argument(
            '--keys',
            required=False,
            action='count',
            help='include repository keys')

    args_parser.add_argument(
            '--ssh',
            required=False,
            action='count',
            help='include ssh keys')

    args_parser.add_argument(
            '--git-repos',
            required=False,
            action='store',
            help='include git repos (Specify path)')

    args_parser.add_argument(
            '--all',
            required=False,
            action='count',
            help='include everything available (Specify git repos path)')

    args_parser.add_argument(
            '-v', '--version',
            action='version',
            version='0.1.0',
            help='print executable version')

    args = args_parser.parse_args()
    print(args)

    if args.action == 'restore':
        restore(args)
    elif args.action == 'backup':
        backup(args)


if __name__ == "__main__":
    main()
