
def log(status, msg):
    """
    Log a message prefixed by a status tag
    """

    print(f"[{status}] {msg}")


def info(msg):
    """
    Log a message prefixed by the INFO status tag
    """

    log("INFO", msg)


def warn(msg):
    """
    Log a message prefixed by the WARN status tag
    """

    log("WARN", msg)


def erro(msg):
    """
    Log a message prefixed by the ERRO status tag
    """

    log("ERRO", msg)


def succ(msg):
    """
    Log a message prefixed by the SUCC status tag
    """

    log("SUCC", msg)


def fail(msg):
    """
    Log a message prefixed by the FAIL status tag
    """

    log("FAIL", msg)


def debu(msg):
    """
    Log a message prefixed by the DEBU status tag
    """

    log("DEBU", msg)
