from modules.clear import clear
from modules.plot import *
from modules.type_write import *
from modules.inventory import *

class Player:
    
    def __init__(self, name: str, pos: list, map_choice: Plot, jacket: Inventory, level: int=1):
        self.name = name
        self.pos = pos
        self.map_choice = map_choice
        self.jacket = jacket
        self.level = level

    def __str__(self):
        return self.name

    def move(self):
        while True:
            if self.map_choice.plot[self.pos[0]][self.pos[1]] != "":
                type_write(f"You are at {self.map_choice.plot[self.pos[0]][self.pos[1]]}.")
            else:
                type_write("There's nothing here.")
            move_choice = type_write("Where would you like to move?\n"
                                + f"({BOLD_START}up{BOLD_END}/{BOLD_START}down{BOLD_END}/{BOLD_START}left{BOLD_END}/{BOLD_START}right{BOLD_END}/{BOLD_START}stop{BOLD_END})", userin=True)
            clear()
            if move_choice == "up" and self.pos[0] > 0:
                self.pos[0] -= 1
                continue
            elif move_choice == "down" and self.pos[0] < len(self.map_choice.plot)-1:
                self.pos[0] += 1
                continue
            elif move_choice == "left" and self.pos[1] > 0:
                self.pos[1] -= 1
                continue
            elif move_choice == "right" and self.pos[1] < len(self.map_choice.plot[0])-1:
                self.pos[1] += 1
                continue
            elif move_choice == "stop":
                break
            clear()
            if move_choice in ["up", "down", "left", "right"]:
                type_write("You are at the edge of the map! ", newline=False)
            else:
                type_write("That's not a valid direction! ", newline=False)
        
    def level_up(self):
        self.level += 1

        # clear()
