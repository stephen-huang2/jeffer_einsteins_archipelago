from modules.clear import clear
from modules.plot import *

class Player:
    
    def __init__(self, name: str, pos: list, map_choice: Plot):
        self.name = name
        self.pos = pos
        self.map_choice = map_choice

    def __str__(self):
        return self.name

    def move(self):
        while True:
            move_choice = input("Where would you like to move?\n"
                                + "(up/down/left/right/stop)\n")
            if move_choice == "up" and self.pos[0] > 0:
                self.pos[0] -= 1
            elif move_choice == "down" and self.pos[0] < len(self.map_choice.plot)-1:
                self.pos[0] += 1
            elif move_choice == "left" and self.pos[1] > 0:
                self.pos[1] -= 1
            elif move_choice == "right" and self.pos[1] < len(self.map_choice.plot[0])-1:
                self.pos[1] += 1
            elif move_choice == "stop":
                break
            elif move_choice in ["up", "down", "left", "right"]:
                print("You have reached the edge of the map.", end=" ")
            else:
                print("That's not a valid direction!", end=" ")
            clear()
            print(f"You are at {self.map_choice.plot[self.pos[0]][self.pos[1]]}.\n")
        clear()
