
def log(status, msg):
    print(f"[{status}] {msg}")


def info(msg):
    log("INFO", msg)


def warn(msg):
    log("WARN", msg)


def erro(msg):
    log("ERRO", msg)


def debu(msg):
    log("DEBU", msg)
