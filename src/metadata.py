import os


def get_desktop_environment():
    desktop_session = os.environ.get('XDG_CURRENT_DESKTOP')
    if desktop_session:
        pair = desktop_session.split(":")
        return [session.strip().lower() for session in pair]
    else:
        # Fallback method to get the session if XDG_CURRENT_DESKTOP is not set
        desktop_session = os.environ.get('DESKTOP_SESSION')
        if desktop_session:
            pair = desktop_session.split(":")
            return [session.strip().lower() for session in pair]
        else:
            return ["Unknown"]


print(get_desktop_environment())


def metadata(key, value):
    metadata = ""
    metadata += "{"
    metadata += f"{key}: {value}"
    metadata += "}"
    return metadata


def shorten(str):
    return f"_{str[0:2]}"
