import sys
import time

BOLD_START = '\033[1m'
BOLD_END = '\033[0m'


def type_write(text: str,
               delay: float = 0.01,
               newline: bool = True,
               userin: bool = False):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    if newline:
        print()
    if userin:
        userin = input()
        return userin
