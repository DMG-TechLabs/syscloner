from logging import erro, warn
from constants import UBUNTU, GNOME, DEBIAN

supported_distros = [
            UBUNTU,
            DEBIAN,
        ]

supported_guis = [
            GNOME
        ]


def check_distro(distro):
    for d in supported_distros:
        if d == distro:
            return True

    return False


def check_gui(gui):
    for d in supported_guis:
        if d == gui:
            return True

    return False


def check_desktop_env(env):
    if not check_distro(env[0]):
        erro(f"Distro '{env[0]}' is not currently supported!")
        return False

    if not check_gui(env[1]):
        erro(f"GUI '{env[1]}'is not currently supported!")
        return False

    return True
