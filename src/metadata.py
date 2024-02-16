import os
import re


def get_desktop_environment():
    desktop_session = os.environ.get('XDG_CURRENT_DESKTOP')
    if desktop_session:
        pair = desktop_session.split(":")
        return [session.strip().lower() for session in pair]
    else:
        # Fallback method to get the session if XDG_CURRENT_DESKTOP is not set
        desktop_session = os.environ.get('DESKTOP_SESSION')
        if desktop_session:
            pair = desktop_session.split("-")
            return [session.strip().lower() for session in pair]
        else:
            return ["Unknown"]


def metadata(key, value):
    metadata = "{"
    metadata += f"{key}: {value}"
    metadata += "}"
    return metadata


def is_metadata(str):
    pattern = r'^\{[^\{\}]+:\s*[^\{\}]+\}$'

    if re.match(pattern, str):
        return True
    else:
        return False


def parse_metadata(str):
    """Parses cvf file's metadata
    From {key: value} to [key, value]
    """

    str = str.strip('{}')
    key, value = str.split(':', 1)

    key = key.strip()
    value = value.strip()

    return [key, value]


def shorten(str):
    return f"_{str[0:2]}"
