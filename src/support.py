from logging import erro, warn
from constants import MANJARO, UBUNTU, XUBUNTU, LUBUNTU, GNOME, DEBIAN, ARCH
from metadata import get_desktop_environment

debian_based = [
    "tails",
    "antix",
    "armbian",
    "astra",
    "av",
    "backbox",
    "bharat",
    "blankon",
    "canaima",
    "commodore",
    "corel",
    "crunchbang",
    "debian",
    "deepin",
    "devuan",
    "doudoulinux",
    "dreamlinux",
    "dyson",
    "elementary",
    "emdebian grip",
    "emmabuntüs",
    "finnix",
    "freedombox",
    "glinux",
    "gnewsense",
    "grml",
    "guadalinex",
    "handylinux",
    "huayra",
    "kaisen",
    "kali",
    "kanotix",
    "knoppix",
    "libranet",
    "limux",
    "linspire",
    "maemo",
    "mepis",
    "musix",
    "mx",
    "openzaurus",
    "pardus",
    "parrot",
    "parsix",
    "proxmox",
    "puavo",
    "pureos",
    "q4os",
    "raspberry pi",
    "slax",
    "solydxk",
    "sonic",
    "sparky",
    "steamos",
    "subgraph",
    "sunwah",
    "turnkey",
    "ubuntu",
    "uruk",
    "userlinux",
    "usu",
    "vyatta",
    "vyos",
    "webconverger",
    "wienux",
]

arch_based = [
    "archbang",
    "archex",
    "archman",
    "arch",
    "archstrike ",
    "arcolinux ",
    "artix",
    "blackarch",
    "bluestar",
    "chimeraos",
    "ctlos",
    "crystal",
    "endeavouros",
    "garuda",
    "hyperbola",
    "instantos",
    "kaos",
    "manjaro",
    "msys2",
    "obarun",
    "parabola",
    "puppyrus-a",
    "rebornos",
    "snal",
    "steamos 3",
    "systemrescue",
    "tearch linux",
    "ubos",
]

supported_distros = [
    UBUNTU,
    DEBIAN,
]

supported_guis = [
    GNOME,
]


def check_distro(distro):
    """
    Checks if user's distro is currently supported by the program
    """

    for d in supported_distros:
        if d == distro:
            return True

    return False


def check_gui(gui):
    """
    Checks if user's gui is currently supported by the program
    """

    for d in supported_guis:
        if d == gui:
            return True

    return False


def check_desktop_env(env):
    """
    Checks if user's distro and gui are currently supported by the program
    """

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


def are_in_same_list(lst, element1, element2):
    return element1 in lst and element2 in lst


def are_distros_compatible(distro1, distro2):
    """
    Returns true if both distros are debian based or arch based
    """

    return are_in_same_list(debian_based, distro1, distro2) or are_in_same_list(arch_based, distro1, distro2)


def is_compatible(metadata):
    """
    Checks if file metadata and desktop environment (distro, gui) are compatible
    """

    env = get_desktop_environment()

    if env[1] != metadata['gui']:
        return False

    if not are_distros_compatible(env[0], metadata['distro']):
        return False

    return True
