from logging import erro, warn
from constants import MANJARO, UBUNTU, GNOME, DEBIAN, ARCH
from metadata import get_desktop_environment

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
    if not check_distro(env[0]) and not check_gui(env[1]):
        erro(f"Distro '{env[0]}' is not currently supported!")
        erro(f"GUI '{env[1]}'is not currently supported!")
        return False

    if not check_distro(env[0]):
        erro(f"Distro '{env[0]}' is not currently supported!")
        return False

    if not check_gui(env[1]):
        erro(f"GUI '{env[1]}'is not currently supported!")
        return False

    return True


def is_compatible(metadata):
    env = get_desktop_environment()

    if env[1] != metadata['gui']:
        return False

    # Temporary solution (We need a method for this)
    if (env[0] == UBUNTU or DEBIAN) and (metadata['distro'] == ARCH or MANJARO):
        return False

    return True
