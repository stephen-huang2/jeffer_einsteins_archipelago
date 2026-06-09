# Imports & Global Variables
from modules.clear import clear
from modules.plot import *
from modules.player import Player
from modules.inventory import *
from modules.type_write import *
from modules.interactable_rooms import Room

# Defining each island in the main map
base = Island("Main Island (Lab)", "1x1", "0,0", "The lab you escaped from.")
forests = Island("Enchanted Woodlands", "1x3", "2,0",
                 "Largely uncharted. Explore at your own risk.")
caves = Island("Jagged Caverns", "3x3", "2,0", "Litterred with corpses of miners.", "0,2")
farms = Island("Crop Meadows", "2x3", "2,0",
               "Scattered with nourishment, from vegetables & grain to all kind's of fruit and some pigs.")
fire_world = Island ("Hellscape", "5x1", "0,4",
                     "None that have ventured are known to return.")
water_world = Island("Aquatic Abyss", "2x1", "0,0",
                     "Try to not get swallowed by the depths of the Abyss.")
prison = Island("Darkwood Prison", "1x1", "0,0", "A prison filled with opportunities.")
dock = Island("Einstein Dock's", "1x1", "0,0", "The dock that leads to freedom.")
spiders = Island("Arachnid Web", "2x2",  "0,0", "Tangled in treacherous spider silk.")

# defining main map
main_map = Plot("MAIN MAP", "3x3", "1,1")

# assigning map coordinates to islands
main_map.plot[0][0] = "LOCKED" # forests
main_map.plot[0][1] = caves
main_map.plot[0][2] = "LOCKED" # farms
main_map.plot[1][0] = "LOCKED" # fire_world
main_map.plot[1][1] = base
main_map.plot[1][2] = "LOCKED" # water_world
main_map.plot[2][0] = "LOCKED" # prison
main_map.plot[2][1] = "LOCKED" # dock
main_map.plot[2][2] = "LOCKED" # spiders

# asssigning caves coordinates to quests.
caves.plot[2][0] = "Cliff"
caves.plot[1][2] = Inventory("Dead Body", inventory=2)
caves.plot[0][2] = Room("Map to the Meadows", True)

# assigning loot stashes for caves
caves.plot[1][2].inventory[0][0] = "1. Key"
caves.plot[1][2].inventory[1][0] = "2. Pocket"

# assigning base coordinates
base.plot[0][0] = "Lab"

# assigning farm coordinates to quests
farms.plot[2][0] = "Farm Gates"
farms.plot[2][1] = Inventory("Tool shed", inventory=1)
farms.plot[0][1] = Inventory("Orchards", inventory=1)
farms.plot[1][1] = Inventory("Farm Land", inventory=1)
farms.plot[0][0] = Inventory("Pigsty", inventory=1)
farms.plot[1][0] = "Empty Farm"

# assigning loot stashes for farms
farms.plot[0][0].inventory[0][0] = "Pork"
farms.plot[1][1].inventory[0][0] = "Bread"
farms.plot[0][1].inventory[0][0] = "Apple"
farms.plot[2][1].inventory[0][0] = "Shovel"

# assigning water world coordinates to quests
water_world.plot[0][0] = "Enternce of Abyss"
water_world.plot[0][1] = "The Kraken"

# assigning fire world coordinates to quests
fire_world.plot[0][4] = "Gates of Hell"
fire_world.plot[0][2] = Inventory("Battlefield", inventory=1)
fire_world.plot[0][0] = "Demon's Palace"

# assigning loot stashes for fire world
fire_world.plot[0][2].inventory[0][0] = "1. Eye of Hell"

# assigning forest coordinates to quests
forests.plot[2][0] = "Enchanted Forest"
forests.plot[0][0] = "Dryad"

# assigning dock coordinates to quests
dock.plot[0][0] = "Grand Boat House"

# assigning prison coordinates to quests
prison.plot[0][0] = "Devil's Hostel"

# assigning spider coordinates to quests
spiders.plot[0][0] = "Cave Entrance"
spiders.plot[0][1] = "Cave Crawlers"
spiders.plot[1][0] = "Web's"
spiders.plot[1][1] = "Arachne"

# Player starts at main island
steve = Player("Steve", [int(main_map.start_pos.split(",")[0]),
                        int(main_map.start_pos.split(",")[1])], main_map, Inventory("Steve's Jacket", 5))


def explore_island(player_name: Player):
    original_position = (player_name.pos).copy()
    
    if type(main_map.plot[player_name.pos[0]][player_name.pos[1]]) == str:
        type_write("You are not ready for this adventure yet...\n")
        return

    player_name.map_choice = main_map.plot[player_name.pos[0]][player_name.pos[1]]
    type_write(f"INFO ({player_name.map_choice}):\n" + player_name.map_choice.description + "\n")
    player_name.pos = [int(player_name.map_choice.start_pos.split(",")[0]),
                int(player_name.map_choice.start_pos.split(",")[1])]
    
    choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
    loot = False
    while True:
        menu_choice = type_write("What would you like to do?\n"
                            + choices, userin=True)
        clear()
        if menu_choice.startswith("move"):
            player_name.move()
        elif menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("inspect"):
            player_name.jacket.view_inventory()
        elif loot and menu_choice.startswith("search"):
            loot_stash = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            loot_stash.view_inventory()
            item_choice = type_write("What would you like to withdraw?\n"
                                     + f"({', '.join([str(i+1) for i in range(len(loot_stash.inventory))])})", userin=True)
            loot_stolen = False
            if item_choice in [str(i+1) for i in range(len(loot_stash.inventory))]:
                for i in range(len(player_name.jacket.inventory)):
                    if player_name.jacket.inventory[i][0][-5:] == "EMPTY":
                        if loot_stash.inventory[int(item_choice)-1][0].split(". ")[1] != "EMPTY" and \
                            loot_stash.inventory[int(item_choice)-1][0].split(". ")[1] != "Pocket":
                            player_name.jacket.inventory[i][0] = f"{i+1}. {loot_stash.inventory[int(item_choice)-1][0].split(". ")[1]}"
                            type_write("Item successfully picked up!\n")
                        elif loot_stash.inventory[int(item_choice)-1][0].split(". ")[1] == "Pocket":
                            type_write("Pocket added to jacket.\n")
                            player_name.jacket.inventory.append([f"{len(player_name.jacket.inventory)+1}. EMPTY"])
                        else:
                            type_write("There's nothing to pick up. \n")
                        loot_stash.inventory[int(item_choice)-1][0] = f"{item_choice}. EMPTY"
                        loot_stolen = True
                        break
                if not loot_stolen:
                    type_write("It appears your pockets are full!\n")
        elif menu_choice.startswith("exit"):
            if player_name.pos == [int(player_name.map_choice.start_pos.split(",")[0]),
                int(player_name.map_choice.start_pos.split(",")[1])]:
                player_name.map_choice = main_map
                player_name.pos = original_position
                type_write(f"You have exited the {main_map.plot[player_name.pos[0]][player_name.pos[1]]} successfully!\n")
                break

            elif player_name.map_choice.end_pos != None and \
            player_name.pos == [int(player_name.map_choice.end_pos.split(",")[0]),
            int(player_name.map_choice.end_pos.split(",")[1])]:
                    player_name.map_choice = main_map
                    player_name.pos = original_position
                    type_write(f"You have exited the {main_map.plot[player_name.pos[0]][player_name.pos[1]]} successfully!\n")
                    break
            else:
                type_write(f"You need to be at an entrance/exit first!\n")
        else:
            type_write("You cannot do that!\n")

        if type(player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]) == Inventory:
            type_write("You are at a loot stash.")
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            loot = True
        else:
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            loot = False

        if type(player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]) == Room:
            key_room = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            if key_room.key:
                type_write("You need a key to proceed.")
                ask_key = type_write(f"Use key?\n({BOLD_START}Y{BOLD_END}/{BOLD_START}N{BOLD_END})", userin=True)
                if ask_key.lower().startswith("y"):
                    for item in player_name.jacket.inventory:
                        if item[0][-3:] == "Key":
                            type_write("You've unlocked the room! You have gained access to a bigger map!")
                            key_room.unlocked = True
                            key_room.key = False
                            item[0] = item[0].split(". ")[0] + ". EMPTY"
                            player_name.level_up()
                            break
                    if not key_room.unlocked:
                        type_write("You do not have a key!")
                # elif ask_key.lower().startswith("n"):


def main():

    while True:
        player_name = type_write(f"Who would you like your player to be?\n({BOLD_START}Steve{BOLD_END})", userin=True)
        if player_name.lower().startswith("steve"):
            player_name = steve
            break
        else:
            clear()
            type_write("That player doesn't exist!")

    clear()

    type_write(f"Hello {player_name.name.capitalize()}~")

    while True:

        if player_name.level >= 2:
            main_map.plot[0][2] = farms

        menu_choice = type_write("What would you like to do?\n"
                            + f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}enter island{BOLD_END}/{BOLD_START}quit{BOLD_END})", userin=True)        
        if menu_choice == "quit":
            type_write(f"\nGood bye, {player_name.name.capitalize()}...")
            break
        
        clear()
        if menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("move"):
            player_name.move()
        elif menu_choice.startswith("enter"):
            explore_island(player_name)
        elif menu_choice.startswith("inspect"):
            player_name.jacket.view_inventory()
        else:
            type_write("You cannot do that!")
