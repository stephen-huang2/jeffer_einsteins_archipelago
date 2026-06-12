import os
from subprocess import run


def clear():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    run(command, shell=True)