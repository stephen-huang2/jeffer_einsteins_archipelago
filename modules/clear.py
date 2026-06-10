from subprocess import run
import os

clear = lambda: run('cls' if os.name == 'nt' else 'clear', shell=True)