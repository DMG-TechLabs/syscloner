
def metadata(key, value):
    metadata = ""
    metadata += "{"
    metadata += f"{key}: {value}"
    metadata += "}"
    return metadata


def get_distro(distro):
    match distro:
        case "_gn":
            return "Gnome"
        case _:
            return None


def get_os(os):
    match os:
        case "_ub":
            return "Ubuntu"
        case _:
            return None
