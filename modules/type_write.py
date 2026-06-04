import sys
import time

def type_write(text: str, delay: float = 0.05, newline: bool=True, userin: bool=False):
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if newline:
        print()
    if userin:
        userin = input()
        return userin