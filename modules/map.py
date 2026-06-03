# Imports & Global Variables
from modules.clear import clear
from modules.plot import *
from modules.player import Player


# Defining each island in the main map
base = Island("Main Island (Base)", "1x1", "0,0", "Your home.")
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

# Player starts at main island
steve = Player("Steve", [int(main_map.start_pos.split(",")[0]),
                        int(main_map.start_pos.split(",")[1])], main_map)


def explore_island(player_name: Player):
    original_position = (player_name.pos).copy()
    
    player_name.map_choice = main_map.plot[player_name.pos[0]][player_name.pos[1]]
    player_name.pos = [int(player_name.map_choice.start_pos.split(",")[0]),
                int(player_name.map_choice.start_pos.split(",")[1])]
    while True:
        menu_choice = input("What would you like to do?\n"
                            + "(move/view map/exit island)\n")
        clear()
        if menu_choice.startswith("move"):
            player_name.move()
        elif menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("exit"):
            player_name.map_choice = main_map
            player_name.pos = original_position
            print(f"You have exited the {main_map.plot[player_name.pos[0]][player_name.pos[1]]} successfully!")
            break
        else:
            print("That's not a valid choice!\n")


def explore_main(player_name: Player):
    while True:
        menu_choice = input("What would you like to do?\n"
                            + "(move/view map/enter island/quit)\n")        
        if menu_choice == "quit":
            print(f"\nGood bye, {player_name.name.upper()}...")
            break
        
        clear()
        if menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("move"):
            player_name.move()
        elif menu_choice.startswith("enter"):
            explore_island(player_name)
        else:
            print("You cannot do that!\n")
