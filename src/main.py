from constants import GNOME, UBUNTU
from file_builder import FileBuilder
from file_parser import FileParser


def main():
    builder = FileBuilder()

    # builder.include_all()
    # builder.include_repository_keys()
    # builder.include_apt_repositories()
    # builder.include_apt_packages()
    # builder.include_snap_packages()
    # builder.include_flatpak_packages()
    builder.include_git_repositories('/home/konstantinos/personal/repos')
    builder.build("kdesp73", UBUNTU, GNOME)

    parser = FileParser("kdesp73_ub_gn.cvf")
    parser.parse()

    # print("apt_packages: ", parser.apt_packages)
    # print("snap_packages: ", parser.snap_packages)
    # print("flatpak_packages: ", parser.flatpak_packages)
    # print("apt_repositories: ", parser.apt_repositories)
    # print("ssh: ", parser.ssh)
    print("git_repos: ", parser.git_repos)

    for pair in parser.git_repos:
        print(pair[0])
        print(pair[1] + "\n")


if __name__ == "__main__":
    main()
