import os


def dir_exist(path: str) -> bool:
    """
    Check if a directory exists. Returns true if it does, false if it doesn't.
    """
    if os.path.exists(path):
        return True
    else:
        return False
