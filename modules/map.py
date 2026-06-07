# Imports & Global Variables
from modules.clear import clear
from modules.plot import *
from modules.player import Player
from modules.inventory import *
from modules.type_write import type_write

# Defining each island in the main map
base = Island("Main Island (Lab)", "1x1", "0,0", "Your home.")
forests = Island("Enchanted Woodlands", "1x3", "2,0",
                 "Largely uncharted. Explore at your own risk.")
caves = Island("Jagged Caverns", "4x4", "3,0", "Litterred with corpses of miners.")
farms = Island("Crop Meadows", "2x3", "2,0",
               "Scattered with nourishment, from vegetables & grain to wild rabbits & chickens.")
fire_world = Island ("Hellscape", "5x1", "0,4",
                     "None that have ventured are known to return.")
water_world = Island("Aquatic Abyss", "2x1", "0,0",
                     "Try to not get swallowed by the depths.")
merchant = Island("Merchant's wares", "1x1", "0,0", "Barter for goods.")
pantheon = Island("Pantheon", "1x1", "0,0", "Draw healing energy from higher powers.")
spiders = Island("Arachnid Web", "2x2",  "0,0", "Tangled in treacherous spider silk.")

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

# asssigning caves coordinates to quests.
'''
TODO -> -player can only exit from hanging rope, if player tries before they have rope it tells them they cant go up
        -make player solve riddle to get a key to open the loot stash
        -put "Rope" in loot stash
'''
caves.plot[0][0] = "Cliff"
caves.plot[0][1] = "     "
caves.plot[1][2] = "Dead Body"
caves.plot[3][1] = Inventory("Loot stash")
caves.plot[3][3] = "Hanging Rope"

base.plot[0][0] = "Lab"

# assigning farm coordinates to quests
farms.plot[2][0] = "Farm Gates"
farms.plot[2][1] = "Tool Garage"
farms.plot[0][1] = " "
farms.plot[1][1] = "Farm Land"
farms.plot[0][0] = "Pigsty"
farms.plot[0][1] = " "

# Player starts at main island
steve = Player("Steve", [int(main_map.start_pos.split(",")[0]),
                        int(main_map.start_pos.split(",")[1])], main_map)


def explore_island(player_name: Player):
    original_position = (player_name.pos).copy()
    
    player_name.map_choice = main_map.plot[player_name.pos[0]][player_name.pos[1]]
    type_write(f"INFO ({player_name.map_choice}):\n" + player_name.map_choice.description + "\n")
    player_name.pos = [int(player_name.map_choice.start_pos.split(",")[0]),
                int(player_name.map_choice.start_pos.split(",")[1])]
    
    choices = "(move/view map/exit island)"
    while True:
        menu_choice = type_write("What would you like to do?\n"
                            + choices, userin=True)
        clear()
        if menu_choice.startswith("move"):
            player_name.move()
        elif menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("exit"):
            if player_name.pos == [int(player_name.map_choice.start_pos.split(",")[0]),
                int(player_name.map_choice.start_pos.split(",")[1])]:
                player_name.map_choice = main_map
                player_name.pos = original_position
                type_write(f"You have exited the {main_map.plot[player_name.pos[0]][player_name.pos[1]]} successfully!")
                break
            else:
                type_write(f"You need to return to the island entrance first!\n")
        else:
            type_write("You cannot do that!\n")

        if type(player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]) == Inventory:
            type_write("Looks like you stumbled across some stuff.")
            choices = "(move/view map/search/exit island)"
        else:
            choices = "(move/view map/exit island)"


def main():

    while True:
        player_name = type_write("Who would you like your player to be?\n(Steve)", userin=True)
        if player_name.lower().startswith("steve"):
            player_name = steve
            break
        else:
            clear()
            type_write("That player doesn't exist!")

    clear()

    type_write("Welcome Steve~")

    while True:
        menu_choice = type_write("What would you like to do?\n"
                            + "(move/view map/enter island/quit)", userin=True)        
        if menu_choice == "quit":
            type_write(f"\nGood bye, {player_name.name.upper()}...")
            break
        
        clear()
        if menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("move"):
            player_name.move()
        elif menu_choice.startswith("enter"):
            explore_island(player_name)
        else:
            type_write("You cannot do that!")
