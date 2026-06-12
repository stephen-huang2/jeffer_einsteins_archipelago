# Imports & Global Variables
from modules.clear import clear
from modules.map import *
from modules.type_write import type_write
from modules.runs import log_run, RUNS_FILE
from datetime import datetime
import csv
import os

# Building the story
clear()
type_write("Welcome~")

# Menu prompt for tutorial and runs log
while True:
    menu_choice = type_write(f"What would you like to do?\n({BOLD_START}tutorial{BOLD_END}/{BOLD_START}runs{BOLD_END}/{BOLD_START}play{BOLD_END})", userin=True)
    
    if menu_choice.lower().startswith("tutorial"):
        clear()
        try:
            with open("tutorial.txt", "r") as tutorial_file:
                type_write(tutorial_file.read())
            type_write("\nPress Enter to continue...", userin=True)
            clear()
        except FileNotFoundError:
            type_write("Tutorial file not found.\n")
    
    elif menu_choice.lower().startswith("runs"):
        clear()
        if os.path.exists(RUNS_FILE):
            try:
                with open(RUNS_FILE, "r") as runs_file:
                    content = runs_file.read()
                    if content.strip():
                        type_write("=== PREVIOUS RUNS ===\n")
                        type_write(content)
                    else:
                        type_write("No runs logged yet.\n")
            except Exception as e:
                type_write(f"Error reading runs log: {e}\n")
        else:
            type_write("No runs log found yet.\n")
        type_write("\nPress Enter to continue...", userin=True)
        clear()
    
    elif menu_choice.lower().startswith("play"):
        clear()
        break
    
    else:
        clear()
        type_write("Invalid choice. Please enter 'tutorial', 'runs', or 'play'.\n")

main()