import sys
import time


BOLD_START = "\033[1m"  # ANSI escape code to begin bold text
BOLD_END = "\033[0m"    # ANSI escape code to reset text formatting


def type_write(
    text: str,
    delay: float = 0.01,
    newline: bool = True,
    userin: bool = False,
):
    """
    Print text with a typewriter effect, one character at a time.

    Args:
        text:    The string to display.
        delay:   Seconds between each character (default 0.01).
        newline: If True, print a newline after the text (default True).
        userin:  If True, prompt for user input after printing and return it (default False).

    Returns:
        The user's input string if userin is True, otherwise None.
    """
    # Print each character one at a time with a short delay
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    if newline:
        print()

    # Capture and return user input if requested
    if userin:
        userin = input()
        return userin