# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:16:38 2026

@author: syed.hussain1
"""

from tabulate import tabulate
import subprocess

class Island:
    
    def __init__(self, name, start_pos, plot, description):
        self.name = name
        self.start_pos = start_pos
        self.plot = Plot(self.name, plot, self.start_pos)
        self.description = description

    
    def __str__(self):
        return self.name

    def view_island(self):
        return tabulate(self.plot, tablefmt="fancy_grid") + "\n"


class Player:
    
    def __init__(self, name, pos, map_choice):
        self.name = name
        self.pos = pos
        self.map_choice = map_choice


class Plot:
    def __init__(self, name, plot, start_pos):
        self.name = name
        self.plot = [[_ for _ in range(int(plot.split("x")[0]))] \
                     for _ in range(int(plot.split("x")[1]))]
        self.start_pos = start_pos
    
        

base = Island("Main Island (Base)", "0,0", "1x1", "Your home.")
forests = Island("Enchanted Woodlands", "2,0", "1x3",
                 "Largely uncharted. Explore at your own risk.")
caves = Island("Jagged Caverns", "3,0", "4x4", "Litterred with corpses of miners.")
farms = Island("Crop Meadows", "2,0", "2x3",
               "Scattered with nourishment, from vegetables & grain to wild rabbits & chickens.")
fire_world = Island ("Hellscape", "0, 4", "5x1",
                     "None that have ventured are known to return.")
water_world = Island("Aquatic Abyss", "0,0", "2x1",
                     "Try to not get swallowed by the depths.")
merchant = Island("Merchant's wares", "0,0", "1x1", "Barter for goods.")
pantheon = Island("Pantheon", "0,0", "1x1", "Draw healing energy from higher powers.")
spiders = Island("Arachnid Web", "0,0", "2x2", "Tangled in treacherous spider silk.")

# defining main map
main_map = Plot("MAIN MAP", "3x3", "1,1")

# assigning map coordinates to islands
main_map.plot[0][0] = forests
main_map.plot[0][1] = caves
main_map.plot[0][2] = farms
main_map.plot[1][0] = fire_world
main_map.plot[1][1] = base
main_map.plot[1][2] = water_world
main_map.plot[2][0] = merchant
main_map.plot[2][1] = pantheon
main_map.plot[2][2] = spiders


# Player starts at main island
steve = Player("Steve", [int(main_map.start_pos.split(",")[0]),
                        int(main_map.start_pos.split(",")[1])], main_map.plot)


def move():
    global steve
    if type(steve.map_choice) == list:
        while True:
            move_choice = input("Where would you like to move?\n"
                                + "(up/down/left/right/stop)\n")
            if move_choice == "up" and steve.pos[0] > 0:
                steve.pos[0] -= 1
            elif move_choice == "down" and steve.pos[0] < len(steve.map_choice)-1:
                steve.pos[0] += 1
            elif move_choice == "left" and steve.pos[1] > 0:
                steve.pos[1] -= 1
            elif move_choice == "right" and steve.pos[1] < len(steve.map_choice[0])-1:
                steve.pos[1] += 1
            elif move_choice == "stop":
                break
            elif move_choice in ["up", "down", "left", "right"]:
                print("Movement is of bounds!", end=" ")
            else:
                print("That's not a valid direction!", end=" ")
            subprocess.run("cls", shell=True)
            print(f"You are at {steve.map_choice[steve.pos[0]][steve.pos[1]]}.\n")
        subprocess.run("cls", shell=True)
    elif type(steve.map_choice) == Plot:
        while True:
            move_choice = input("Where would you like to move?\n"
                                + "(up/down/left/right/stop)\n")
            if move_choice == "up" and steve.pos[0] > 0:
                steve.pos[0] -= 1
            elif move_choice == "down" and steve.pos[0] < len(steve.map_choice.plot)-1:
                steve.pos[0] += 1
            elif move_choice == "left" and steve.pos[1] > 0:
                steve.pos[1] -= 1
            elif move_choice == "right" and steve.pos[1] < len(steve.map_choice.plot[0])-1:
                steve.pos[1] += 1
            elif move_choice == "stop":
                break
            elif move_choice in ["up", "down", "left", "right"]:
                print("Movement is of bounds!", end=" ")
            else:
                print("That's not a valid direction!", end=" ")
            subprocess.run("cls", shell=True)
            print(f"You are at {steve.map_choice.plot[steve.pos[0]][steve.pos[1]]}.\n")
        subprocess.run("cls", shell=True)


def view_map():
    print("- THE MAP")
    if type(steve.map_choice) == list:
        print(tabulate(steve.map_choice, tablefmt="fancy_grid") + "\n")
        print(f"You are at {steve.map_choice[steve.pos[0]][steve.pos[1]]}.\n")
    elif type(steve.map_choice) == Plot:
        print(f"- {steve.map_choice.name.upper()}")
        print(tabulate(steve.map_choice.plot, tablefmt="fancy_grid") + "\n")
        print(f"You are at {steve.map_choice.plot[steve.pos[0]][steve.pos[1]]}.\n")

def explore_island():
    steve.map_choice = main_map.plot[steve.pos[0]][steve.pos[1]].plot
    steve.pos = [int(steve.map_choice.start_pos.split(",")[0]),
                int(steve.map_choice.start_pos.split(",")[1])]
    while True:
        menu_choice = input("What would you like to do?\n"
                            + "(move/view map/return to base)\n")
        if menu_choice.startswith("move"):
            subprocess.run("cls", shell=True)
            move()
        elif menu_choice.startswith("view"):
            subprocess.run("cls", shell=True)
            view_map()
        elif menu_choice.startswith("return"):
            subprocess.run("cls", shell=True)
            return_to_base()
            break
        else:
            subprocess.run("cls", shell=True)
            print("That's not a valid choice!\n")

def return_to_base():
    steve.map_choice = main_map.plot
    steve.pos = [1,1]

def main():
    while True:
        menu_choice = input("What would you like to do?\n"
                            + "(move/view map/enter island/quit)\n")        
        if menu_choice == "quit":
            print("\nGood bye, player...")
            break
        elif menu_choice.startswith("view"):
            subprocess.run("cls", shell=True)
            view_map()
        elif menu_choice.startswith("move"):
            subprocess.run("cls", shell=True)
            move()
        elif menu_choice.startswith("enter"):
            subprocess.run("cls", shell=True)
            explore_island()
        else:
            subprocess.run("cls", shell=True)
            print("You cannot do that!\n")

subprocess.run("cls", shell=True)
print("Welcome~")
main()