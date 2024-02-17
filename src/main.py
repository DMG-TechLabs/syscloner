import argparse
from file_builder import FileBuilder
from file_parser import FileParser
from installer import Installer
from metadata import get_desktop_environment
from support import check_desktop_env, is_compatible
from logger import debu, info, succ, erro

def restore(args):
    """
    Parses the file provided from the command line and then installs everything depending on the options provided

    Parameters
    ----------
    args: argparse arguments
        command line arguments
    """

    parser = FileParser(args.filename)
    parser.parse()

    if not is_compatible(parser.file_metadata):
        erro("Not a compatible file for your system")
        exit(1)

    info("Parsing completed successfully")
    installer = Installer(parser)

    if args.all is not None:
        installer.include_all()
        installer.install()
        succ("Installation complete")
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

    if args.apt_repos is not None:
        installer.include_apt_repositories()

    installer.install()
    succ("Installation complete")


def backup(args):
    """
    Writes the system's information to a cvf file depending on the arguments
    provided from the command line

    Parameters
    ----------
    args: argparse arguments
        command line arguments
    """
    
    builder = FileBuilder()
    desktop_env = get_desktop_environment()
    if args.all is not None:
        info("Including all available options")
        builder.include_all(args.git_repos)

        if not check_desktop_env(desktop_env):
            exit(1)
        else:
            builder.build(args.filename, desktop_env[0], desktop_env[1])
            succ("File written successfully")
            return

    if args.system is not None:
        info("System settings included")
        builder.include_system_settings()

    if args.apt is not None:
        info("Apt packages included")
        builder.include_apt_packages()

    if args.snap is not None:
        info("Snap packages included")
        builder.include_snap_packages()

    if args.flatpak is not None:
        info("Flatpak packages included")
        builder.include_flatpak_packages()

    if args.themes is not None:
        info("Shell themes included")
        builder.include_shell_themes()

    if args.exts is not None:
        info("Gnome extensions included")
        builder.include_gnome_extensions()

    if args.keys is not None:
        info("Keys included")
        builder.include_repository_keys()

    if args.ssh is not None:
        info("SSH included")
        builder.include_ssh()

    if args.git_repos is not None:
        info("Git repositories included")
        builder.include_git_repositories(args.git_repos)

    if args.apt_repos is not None:
        info("Apt repositories included")
        builder.include_apt_repositories()

    if not check_desktop_env(desktop_env):
        exit(1)
    else:
        builder.build(args.filename, desktop_env[0], desktop_env[1])
        succ("File written successfully")


def main():
    args_parser = argparse.ArgumentParser(
            prog='system-cloner',
            description='A configurable tool to backup and restore your linux system from a single file',
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
            '--apt-repos',
            required=False,
            action='count',
            help='include apt repos')

    args_parser.add_argument(
            '--all',
            required=False,
            action='count',
            help='include everything available (Specify git repos path)')

    args_parser.add_argument(
            '-v', '--version',
            action='version',
            version='syscloner 0.1.0',
            help='print executable version')

    args = args_parser.parse_args()
    debu(args)

    if args.action == 'restore':
        restore(args)
    elif args.action == 'backup':
        backup(args)


if __name__ == "__main__":
    main()
