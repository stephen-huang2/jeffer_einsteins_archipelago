# Imports & Global Variables
from modules.clear import clear
from modules.plot import *
from modules.player import Player
from modules.inventory import *
from modules.type_write import *
from modules.interactable_rooms import Room, Dryad, Kraken, DemonsPalace
from modules.hunger import Hunger

# Defining each island in the main map
base = Island("Main Island (Lab)", "1x1", ["0,0"], "The lab you escaped from.")
forests = Island("Enchanted Woodlands", "1x3", ["2,0"],
                 "Largely uncharted. Explore at your own risk.")
caves = Island("Jagged Caverns", "3x3", ["2,0", "0,2", "1,0"], "Litterred with corpses of miners.")
farms = Island("Crop Meadows", "2x3", ["2,0"],
               "Scattered with nourishment, from vegetables & grain to all kind's of fruit and some pigs.")
fire_world = Island ("Hellscape", "5x1", ["0,4"],
                     "None that have ventured are known to return.")
water_world = Island("Aquatic Abyss", "2x1", ["0,0"],
                     "Try to not get swallowed by the depths of the Abyss.")
prison = Island("Darkwood Prison", "1x1", ["0,0"], "A prison filled with opportunities.")
dock = Island("Einstein Dock's", "1x1", ["0,0"], "The dock that leads to freedom.")
spiders = Island("Arachnid Web", "2x2", ["0,0"], "Tangled in treacherous spider silk.")

# defining main map
main_map = Plot("MAIN MAP", "3x2", ["1,1"])

# assigning map coordinates to islands
main_map.plot[0][0] = "LOCKED"  # forests
main_map.plot[0][1] = Room("LOCKED (go here)", True)
main_map.plot[0][2] = "LOCKED"  # farms
main_map.plot[1][0] = "LOCKED"  # fire_world
main_map.plot[1][1] = base
main_map.plot[1][2] = "LOCKED"  # water_world

'''
main_map.plot[2][0] = "LOCKED"  # prison
main_map.plot[2][1] = "LOCKED"  # dock
main_map.plot[2][2] = "LOCKED"  # spiders
'''

# assigning caves coordinates to quests
caves.plot[2][0] = "Cliff"
caves.plot[1][2] = Inventory("Dead body", inventory=2)
caves.plot[0][1] = Inventory("Lost goods", inventory=1)
caves.plot[0][2] = Room("Hanging Rope", True, key_type="Rope")
caves.plot[1][0] = Room("Mysterious Tunnel", True)

# assigning loot stashes for caves
caves.plot[1][2].inventory[0][0] = "1. Key"
caves.plot[1][2].inventory[1][0] = "2. Pocket"
caves.plot[0][1].inventory[0][0] = "1. Rope"

# assigning base coordinates
base.plot[0][0] = Inventory("Lab", 1)
base.plot[0][0].inventory[0][0] = "1. Key"

# assigning farm coordinates to quests
farms.plot[2][0] = "Farm Gates"
farms.plot[2][1] = Inventory("Tool shed", inventory=1)
farms.plot[0][1] = Inventory("Orchards", inventory=1)
farms.plot[1][1] = Inventory("Farm Land", inventory=1)
farms.plot[0][0] = Inventory("Pigsty", inventory=1)
farms.plot[1][0] = "Big Hole"

# assigning loot stashes for farms
farms.plot[0][0].inventory[0][0] = "Pork"
farms.plot[1][1].inventory[0][0] = "Bread"
farms.plot[0][1].inventory[0][0] = "Apple"
farms.plot[2][1].inventory[0][0] = "Shovel"

# assigning water world coordinates to quests
water_world.plot[0][0] = "Entrance of Abyss"
water_world.plot[0][1] = Kraken()

# assigning fire world coordinates to quests
fire_world.plot[0][4] = "Gates of Hell"
fire_world.plot[0][2] = Inventory("Battlefield", inventory=1)
fire_world.plot[0][0] = DemonsPalace()

# assigning loot stashes for fire world
fire_world.plot[0][2].inventory[0][0] = "1. Eye of Hell"

# assigning forest coordinates to quests
forests.plot[2][0] = Inventory("Enchanted Forest", inventory=1)
forests.plot[2][0].inventory[0][0] = "1. Magical Branch"
forests.plot[0][0] = Dryad()

'''
# assigning dock coordinates to quests
dock.plot[0][0] = "Grand Boat House"

# assigning prison coordinates to quests
prison.plot[0][0] = "Devil's Hostel"

# assigning spider coordinates to quests
spiders.plot[0][0] = "Cave Entrance"
spiders.plot[0][1] = "Cave Crawlers"
spiders.plot[1][0] = "Web's"
spiders.plot[1][1] = "Arachne"
'''

# Player starts at main island
steve = Player("Steve", [int(main_map.start_pos[0].split(",")[0]),
                        int(main_map.start_pos[0].split(",")[1])], main_map, Inventory("Steve's Jacket", 5))


def explore_island(player_name: Player):
    original_position = (player_name.pos).copy()

    if type(main_map.plot[player_name.pos[0]][player_name.pos[1]]) == str:
        type_write("You are not ready for this adventure yet...\n")
        return

    player_name.map_choice = main_map.plot[player_name.pos[0]][player_name.pos[1]]
    type_write(f"INFO ({player_name.map_choice}):\n" + player_name.map_choice.description + "\n")
    player_name.pos = [int(player_name.map_choice.start_pos[0].split(",")[0]),
                int(player_name.map_choice.start_pos[0].split(",")[1])]

    choices = ""
    def refresh_location_state():
        nonlocal choices
        current = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
        type_write(player_name.hunger.get_status())
        if type(current) == Inventory:
            type_write("You are at a loot stash.")
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
        elif type(current) == Dryad:
            type_write("The Dryad looms before you.")
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}interact{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
        elif type(current) == Kraken:
            type_write("The Kraken stirs in the deep below you.")
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}interact{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
        elif type(current) == DemonsPalace:
            type_write("The Demon's Palace stands before you, its gates scorched black.")
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}interact{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
        elif type(current) == Room:
            key_room = current
            if key_room.key:
                type_write(f"You are at a locked room. You need a {key_room.key_type} to proceed.")
                choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}use {key_room.key_type}{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            else:
                choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
        else:
            choices = f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
        return current

    current = refresh_location_state()

    while True:
        menu_choice = type_write("What would you like to do?\n"
                                 + choices, userin=True)
        clear()

        if menu_choice.startswith("move"):
            alive = player_name.move()
            if not alive:
                type_write("You collapse from starvation... Einstein finds you.\n")
                type_write("GAME OVER: You starved to death!\n")
                while True:
                    game_choice = type_write("Would you like to quit or restart?\n"
                                            + f"({BOLD_START}quit{BOLD_END}/{BOLD_START}restart{BOLD_END})", userin=True)
                    if game_choice.lower().startswith("quit"):
                        return "game_over"
                    elif game_choice.lower().startswith("restart"):
                        return "restart"
                    clear()
                    type_write("Invalid choice!\n")

        elif menu_choice.startswith("view"):
            player_name.map_choice.view_plot()

        elif menu_choice.startswith("inspect"):
            player_name.jacket.view_inventory()

        elif menu_choice.startswith("use"):
            current = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            if type(current) == Room and current.key:
                key_found = False
                for item in player_name.jacket.inventory:
                    if current.key_type in item[0]:
                        type_write("You've unlocked the room! You have gained access to a bigger map!\n")
                        current.unlocked = True
                        current.key = False
                        item[0] = item[0].split(". ")[0] + ". EMPTY"
                        player_name.level_up()
                        key_found = True
                        break
                if not key_found:
                    type_write(f"You don't have a {current.key_type}!\n")
            else:
                type_write("There is no locked room here.\n")

        elif menu_choice.startswith("interact"):
            current = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]

            if type(current) == Dryad:
                if not current.riddle_solved:
                    has_branch = any("Magical Branch" in item[0] for item in player_name.jacket.inventory)
                    if has_branch:
                        type_write("You offer the Magical Branch. The Dryad accepts it and regards you with ancient eyes.\n")
                        if current.attempt_riddle(type_write, BOLD_START, BOLD_END):
                            for item in player_name.jacket.inventory:
                                if "Magical Branch" in item[0]:
                                    item[0] = item[0].split(". ")[0] + ". EMPTY"
                                    break
                            player_name.level_up()
                        else:
                            type_write("The Dryad rejects your magical branch.\n")
                    else:
                        type_write("The Dryad stares at you coldly.\n\"Bring me a Magical Branch as tribute before I will speak with you.\"\n")
                else:
                    type_write("The Dryad nods at you slowly. You have already proven yourself.\n")

            elif type(current) == Kraken:
                if not current.riddle_solved:
                    if current.attempt_riddle(type_write, BOLD_START, BOLD_END):
                        player_name.level_up()
                else:
                    type_write("The Kraken's eye slides toward you. It has already deemed you worthy.\n")

            elif type(current) == DemonsPalace:
                if not current.riddle_solved:
                    has_eye = any("Eye of Hell" in item[0] for item in player_name.jacket.inventory)
                    if has_eye:
                        type_write("You hold out the Eye of Hell. The palace gates shudder and groan open...\n")
                        if current.attempt_riddle(type_write, BOLD_START, BOLD_END):
                            for item in player_name.jacket.inventory:
                                if "Eye of Hell" in item[0]:
                                    item[0] = item[0].split(". ")[0] + ". EMPTY"
                                    break
                            type_write(
                                "\nYou have escaped back to the real world but you can't find anyone alive around you,\n"
                                "the world seems to be empty and you are the last human being alive......\n"
                            )
                            return "game_over"
                        else:
                            type_write("The demons reject your offering. The Eye of Hell remains with you.\n")
                    else:
                        type_write("The palace gates do not move. Something is missing...\n\"Bring us the Eye of Hell.\"\n")
                else:
                    type_write("The demons watch you in silence. You have already passed their test.\n")

            else:
                type_write("There is nothing to interact with here.\n")

        elif menu_choice.startswith("search"):
            current = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            if type(current) == Inventory:
                loot_stash = current
                loot_stash.view_inventory()
                item_choice = type_write("What would you like to withdraw?\n"
                                         + f"({', '.join([str(i+1) for i in range(len(loot_stash.inventory))])})", userin=True)
                loot_stolen = False
                if item_choice in [str(i+1) for i in range(len(loot_stash.inventory))]:
                    for i in range(len(player_name.jacket.inventory)):
                        if player_name.jacket.inventory[i][0][-5:] == "EMPTY":
                            if loot_stash.inventory[int(item_choice)-1][0].split(". ")[1] != "EMPTY" and \
                                    loot_stash.inventory[int(item_choice)-1][0].split(". ")[1] != "Pocket":
                                player_name.jacket.inventory[i][0] = f"{i+1}. {loot_stash.inventory[int(item_choice)-1][0].split('. ')[1]}"
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
            else:
                type_write("There is no loot stash here.\n")

        elif menu_choice.startswith("eat"):
            food_found = False
            food_items = []
            for idx, item in enumerate(player_name.jacket.inventory):
                if item[0][-5:] != "EMPTY" and item[0].split(". ")[1] in ["Pork", "Bread", "Apple"]:
                    food_items.append((idx, item[0]))
                    food_found = True
            
            if not food_found:
                type_write("You have no food in your inventory!\n")
            else:
                type_write("What would you like to eat?\n")
                for i, (idx, food) in enumerate(food_items):
                    type_write(f"{i+1}. {food}")
                food_choice = type_write("Choose an option: ", userin=True)
                
                if food_choice in [str(i+1) for i in range(len(food_items))]:
                    chosen_idx = int(food_choice) - 1
                    item_idx, food_name = food_items[chosen_idx]
                    food_type = food_name.split(". ")[1]
                    success, restore_amount = player_name.hunger.eat(food_type)
                    if success:
                        type_write(f"You eat the {food_type} and restore {restore_amount} hunger points!\n")
                        player_name.jacket.inventory[item_idx][0] = f"{item_idx+1}. EMPTY"
                    else:
                        type_write("You cannot eat that!\n")
                else:
                    type_write("Invalid choice!\n")

        elif menu_choice.startswith("exit"):
            for i in player_name.map_choice.start_pos:
                # print(i.split(","))
                if player_name.pos == [int(i.split(",")[0]),
                    int(i.split(",")[1])]:
                    player_name.map_choice = main_map
                    player_name.pos = original_position
                    type_write(f"You have exited the {main_map.plot[player_name.pos[0]][player_name.pos[1]]} successfully!\n")
                    return
            
            type_write(f"You need to be at an entrance/exit first!\n")
        
        else:
            type_write("You cannot do that!\n")

        current = refresh_location_state()

        # if type(player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]) == Room:
        #     key_room = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
        #     if key_room.key:
        #         type_write(f"You need a {key_room.key_type} to proceed.")
        #         ask_key = type_write(f"Use {key_room.key_type}?\n({BOLD_START}Y{BOLD_END}/{BOLD_START}N{BOLD_END})", userin=True)
        #         if ask_key.lower().startswith("y"):
        #             for item in player_name.jacket.inventory:
        #                 if item[0].split(". ")[1] == key_room.key_type:
        #                     type_write("You've unlocked the room! You have gained access to a bigger map!\n")
        #                     key_room.unlocked = True
        #                     key_room.key = False
        #                     item[0] = item[0].split(". ")[0] + ". EMPTY"
        #                     player_name.level_up()
        #                     player_name.map_choice.start_pos.append
        #                     break
        #             if not key_room.unlocked:
        #                 type_write(f"You do not have a {key_room.key_type}!\n ")


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

        main_map.plot[1][0] = fire_world

        if player_name.level >= 1:
            main_map.plot[0][1] = caves
        if player_name.level >= 2:
            main_map.plot[0][2] = farms
        if player_name.level >= 3:
            main_map.plot[0][0] = forests
        if player_name.level >= 4:
            main_map.plot[1][2] = water_world
        if player_name.level >= 5:
            main_map.plot[1][0] = fire_world

        menu_choice = type_write("What would you like to do?\n"
                                 + f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}enter island{BOLD_END}/{BOLD_START}quit{BOLD_END})", userin=True)
        if menu_choice == "quit":
            type_write(f"\nGood bye, {player_name.name.capitalize()}...")
            break

        clear()
        if menu_choice.startswith("view"):
            player_name.map_choice.view_plot()
        elif menu_choice.startswith("move"):
            alive = player_name.move()
            if not alive:
                type_write("You collapse from starvation... Einstein finds you.\n")
                type_write("GAME OVER: You starved to death!\n")
                while True:
                    game_choice = type_write("Would you like to quit or restart?\n"
                                            + f"({BOLD_START}quit{BOLD_END}/{BOLD_START}restart{BOLD_END})", userin=True)
                    if game_choice.lower().startswith("quit"):
                        type_write(f"\nGood bye, {player_name.name.capitalize()}...")
                        return
                    elif game_choice.lower().startswith("restart"):
                        player_name = steve
                        player_name.hunger = Hunger()
                        break
                    clear()
                    type_write("Invalid choice!\n")
        elif menu_choice.startswith("enter"):
            result = explore_island(player_name)
            if result == "game_over":
                break
            elif result == "restart":
                player_name = steve
                player_name.hunger = Hunger()
        elif menu_choice.startswith("inspect"):
            player_name.jacket.view_inventory()
        else:
            type_write("You cannot do that!")

        if type(player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]) == Room:
            key_room = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            if key_room.key:
                type_write(f"You need a {key_room.key_type} to proceed.")
                ask_key = type_write(f"Use {key_room.key_type}?\n({BOLD_START}Y{BOLD_END}/{BOLD_START}N{BOLD_END})", userin=True)
                if ask_key.lower().startswith("y"):
                    for item in player_name.jacket.inventory:
                        if item[0][-3:] == key_room.key_type:
                            type_write("You've unlocked the room! You have gained access to a bigger map!\n")
                            key_room.unlocked = True
                            key_room.key = False
                            item[0] = item[0].split(". ")[0] + ". EMPTY"
                            player_name.level_up()
                            break
                    if not key_room.unlocked:
                        type_write("You do not have a key!\n")