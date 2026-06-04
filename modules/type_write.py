import sys
import time

def type_write(text: str, delay: float = 0.05, newline: bool=True):
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    if newline:
        print()