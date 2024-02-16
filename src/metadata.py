import os
import re


def get_desktop_environment():
    """
    Returns the desktop environment as an array [distro, gui]
    """
    
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
    """
    Returns a string of the key value pair to be written in the cvf file
    
    Example: key = 'name', value = 'test'
    Returns: {name: test}
    """

    metadata = "{"
    metadata += f"{key}: {value}"
    metadata += "}"
    return metadata


def is_metadata(str):
    """
    Checks if a string is in cvf metadata form using a regular expression
    """

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
    """
    Adds an underscore in front of a string after applying the lowercase method and taking only the first two characters

    Examples: str = Gnome
    Returns: _gn
    """

    return f"_{str[0:2].lower()}"
