import os
import re


def get_desktop_environment():
    """
    Returns
    -------
    list
        the desktop environment as [distro, gui]
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
    Make metadata string from a key value pair

    Parameters
    ----------
    key: string
    value: any

    Returns
    -------
    string
        key value pair to be written in the cvf file ({key: value})
    """

    metadata = "{"
    metadata += f"{key}: {value}"
    metadata += "}"
    return metadata


def is_metadata(str):
    """
    Checks if a string is in cvf metadata form using a regular expression
    
    Parameters
    ----------
    str: string
        string to check if it is formatted as cvf metadata

    Returns
    -------
    boolean
        true if string is formated as a cvf metadata
    """

    pattern = r'^\{[^\{\}]+:\s*[^\{\}]+\}$'

    if re.match(pattern, str):
        return True
    else:
        return False


def parse_metadata(str):
    """
    Parses cvf file's metadata

    Parameters
    ----------
    str: string
        cvf metadata string to parse

    Returns
    -------
    list
        [key, value]
    """

    str = str.strip('{}')
    key, value = str.split(':', 1)

    key = key.strip()
    value = value.strip()

    return [key, value]


def shorten(str):
    """
    Shorten the string to append it to the filename

    Adds an underscore in front of a string after applying the lowercase
    method and taking only the first two characters

    Parameters
    ----------
    str: string
        string to shorten

    Returns
    -------
    string
        shortened string (example: str=Gnome returns `_gn`)
    """

    return f"_{str[0:2].lower()}"
