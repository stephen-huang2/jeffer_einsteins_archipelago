from modules.clear import clear
from modules.plot import *
from modules.type_write import *

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
                type_write("You have reached the edge of the map.", newline=False)
                '''
                TODO -> make this line stay while showing the player where they are (Beacuse it deletes this line rn after telling player where they are)
                '''
            else:
                type_write("That's not a valid direction!", newline=False)
            clear()
            if self.map_choice.plot[self.pos[0]][self.pos[1]] != "":
                type_write(f"You are at {self.map_choice.plot[self.pos[0]][self.pos[1]]}.\n")
            else:
                type_write("There's nothing here.")

        clear()
