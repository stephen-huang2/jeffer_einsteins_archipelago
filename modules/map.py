# Imports & Global Variables
from modules.clear import clear
from modules.plot import *
from modules.player import Player
from modules.inventory import *
from modules.type_write import *
from modules.interactable_rooms import Room, Dryad, Kraken, DemonsPalace
from modules.hunger import Hunger
from modules.runs import log_run
from datetime import datetime


# ---------------------------------------------------------------------------
# Island & Map Definitions
# ---------------------------------------------------------------------------

# Defining each island in the main map
base = Island("Main Island (Lab)", "1x1", ["0,0"], "The lab you escaped from.")
forests = Island(
    "Enchanted Woodlands", "1x3", ["2,0"],
    "Largely uncharted. Explore at your own risk.",
)
caves = Island(
    "Jagged Caverns", "3x3", ["2,0", "0,2", "1,0"],
    "Litterred with corpses of miners.",
)
farms = Island(
    "Crop Meadows", "2x3", ["2,0"],
    "Scattered with nourishment, from vegetables & grain to all kind's of fruit and some pigs.",
)
fire_world = Island(
    "Hellscape", "5x1", ["0,4"],
    "None that have ventured are known to return.",
)
water_world = Island(
    "Aquatic Abyss", "2x1", ["0,0"],
    "Try to not get swallowed by the depths of the Abyss.",
)

# Unused islands — reserved for future content
prison = Island("Darkwood Prison", "1x1", ["0,0"], "A prison filled with opportunities.")
dock = Island("Einstein Dock's", "1x1", ["0,0"], "The dock that leads to freedom.")
spiders = Island("Arachnid Web", "2x2", ["0,0"], "Tangled in treacherous spider silk.")


# ---------------------------------------------------------------------------
# Main Map Layout
# ---------------------------------------------------------------------------

# Defining the main map grid
main_map = Plot("MAIN MAP", "3x2", ["1,1"])

# Assigning map coordinates to islands (unlocked as the player levels up)
main_map.plot[0][0] = "LOCKED"                     # forests
main_map.plot[0][1] = Room("LOCKED (go here)", True)
main_map.plot[0][2] = "LOCKED"                     # farms
main_map.plot[1][0] = "LOCKED"                     # fire_world
main_map.plot[1][1] = base
main_map.plot[1][2] = "LOCKED"                     # water_world

# Planned future map slots (currently unused)
'''
main_map.plot[2][0] = "LOCKED"  # prison
main_map.plot[2][1] = "LOCKED"  # dock
main_map.plot[2][2] = "LOCKED"  # spiders
'''


# ---------------------------------------------------------------------------
# Caves Layout
# ---------------------------------------------------------------------------

# Assigning cave coordinates to locations and quests
caves.plot[2][0] = "Cliff"
caves.plot[1][2] = Inventory("Dead body", inventory=2)
caves.plot[0][1] = Inventory("Lost goods", inventory=1)
caves.plot[0][2] = Room("Hanging Rope", True, key_type="Rope")
caves.plot[1][0] = Room("Mysterious Tunnel", True)

# Assigning loot stashes for caves
caves.plot[1][2].inventory[0][0] = "1. Key"
caves.plot[1][2].inventory[1][0] = "2. Pocket"
caves.plot[0][1].inventory[0][0] = "1. Rope"


# ---------------------------------------------------------------------------
# Base Layout
# ---------------------------------------------------------------------------

# Assigning base coordinates and starting loot
base.plot[0][0] = Inventory("Lab", 1)
base.plot[0][0].inventory[0][0] = "1. Key"


# ---------------------------------------------------------------------------
# Farms Layout
# ---------------------------------------------------------------------------

# Assigning farm coordinates to locations and quests
farms.plot[2][0] = "Farm Gates"
farms.plot[2][1] = Inventory("Tool shed", inventory=1)
farms.plot[0][1] = Inventory("Orchards", inventory=1)
farms.plot[1][1] = Inventory("Farm Land", inventory=1)
farms.plot[0][0] = Inventory("Pigsty", inventory=1)
farms.plot[1][0] = "Big Hole"

# Assigning loot stashes for farms
farms.plot[0][0].inventory[0][0] = "1. Pork"
farms.plot[1][1].inventory[0][0] = "1. Bread"
farms.plot[0][1].inventory[0][0] = "1. Apple"
farms.plot[2][1].inventory[0][0] = "1. Shovel"


# ---------------------------------------------------------------------------
# Water World Layout
# ---------------------------------------------------------------------------

# Assigning water world coordinates to locations and quests
water_world.plot[0][0] = "Entrance of Abyss"
water_world.plot[0][1] = Kraken()


# ---------------------------------------------------------------------------
# Fire World Layout
# ---------------------------------------------------------------------------

# Assigning fire world coordinates to locations and quests
fire_world.plot[0][4] = "Gates of Hell"
fire_world.plot[0][2] = Inventory("Battlefield", inventory=1)
fire_world.plot[0][0] = DemonsPalace()

# Assigning loot stashes for fire world
fire_world.plot[0][2].inventory[0][0] = "1. Eye of Hell"


# ---------------------------------------------------------------------------
# Forest Layout
# ---------------------------------------------------------------------------

# Assigning forest coordinates to locations and quests
forests.plot[2][0] = Inventory("Enchanted Forest", inventory=1)
forests.plot[0][0] = Dryad()

# Assigning loot stashes for forests
forests.plot[2][0].inventory[0][0] = "1. Magical Branch"


# ---------------------------------------------------------------------------
# Player Initialisation
# ---------------------------------------------------------------------------

# Player starts at the main island, at the map's defined start position
steve = Player(
    "Steve",
    [
        int(main_map.start_pos[0].split(",")[0]),
        int(main_map.start_pos[0].split(",")[1]),
    ],
    main_map,
    Inventory("Steve's Jacket", 5),
)


# ---------------------------------------------------------------------------
# Game Functions
# ---------------------------------------------------------------------------

def reset_game(player_name: Player):
    """Reset all game state to initial conditions for a new run."""

    # Clear the terminal
    clear()

    # Reset player state
    player_name.level = 0
    player_name.pos = [
        int(main_map.start_pos[0].split(",")[0]),
        int(main_map.start_pos[0].split(",")[1]),
    ]
    player_name.map_choice = main_map
    player_name.hunger = Hunger()
    player_name.failed_riddle_attempts = 0

    # Reset player inventory to exactly the original 5 slots
    player_name.jacket.inventory = [[f"{i + 1}. EMPTY"] for i in range(5)]

    # Reset all NPCs' riddle_solved states
    forests.plot[0][0].riddle_solved = False
    caves.plot[0][2].riddle_solved = False
    water_world.plot[0][1].riddle_solved = False
    fire_world.plot[0][0].riddle_solved = False

    # Reset all room keys and unlock states
    caves.plot[0][2].key = True
    caves.plot[0][2].unlocked = False
    caves.plot[1][0].key = True
    caves.plot[1][0].unlocked = False
    main_map.plot[0][1].key = True
    main_map.plot[0][1].unlocked = False

    # Reset loot stashes to their original contents
    caves.plot[1][2].inventory[0][0] = "1. Key"
    caves.plot[1][2].inventory[1][0] = "2. Pocket"
    caves.plot[0][1].inventory[0][0] = "1. Rope"

    base.plot[0][0].inventory[0][0] = "1. Key"

    farms.plot[0][0].inventory[0][0] = "1. Pork"
    farms.plot[1][1].inventory[0][0] = "1. Bread"
    farms.plot[0][1].inventory[0][0] = "1. Apple"
    farms.plot[2][1].inventory[0][0] = "1. Shovel"

    fire_world.plot[0][2].inventory[0][0] = "1. Eye of Hell"

    forests.plot[2][0].inventory[0][0] = "1. Magical Branch"

    # Reset main map to its locked initial state
    main_map.plot[0][0] = "LOCKED"
    main_map.plot[0][1] = Room("LOCKED (go here)", True)
    main_map.plot[0][2] = "LOCKED"
    main_map.plot[1][0] = "LOCKED"
    main_map.plot[1][2] = "LOCKED"


def explore_island(player_name: Player):
    """Handle the explore island loop for the current island."""

    # Remember original position so we can return to it on exit
    original_position = (player_name.pos).copy()

    # Prevent entering a locked island slot
    if type(main_map.plot[player_name.pos[0]][player_name.pos[1]]) == str:
        type_write("You are not ready for this adventure yet...\n")
        return

    # Enter the island and display its description
    player_name.map_choice = main_map.plot[player_name.pos[0]][player_name.pos[1]]
    type_write(f"INFO ({player_name.map_choice}):\n" + player_name.map_choice.description + "\n")
    player_name.pos = [
        int(player_name.map_choice.start_pos[0].split(",")[0]),
        int(player_name.map_choice.start_pos[0].split(",")[1]),
    ]

    # Holds the current action choices string, updated each loop
    choices = ""

    def refresh_location_state():
        """Refresh the display and action choices based on the current tile."""
        nonlocal choices
        current = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
        type_write(player_name.hunger.get_status())

        if type(current) == Inventory:
            type_write("You are at a loot stash.")
            choices = (
                f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/"
                f"{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            )
        elif type(current) == Dryad:
            type_write("The Dryad looms before you.")
            choices = (
                f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}interact{BOLD_END}/"
                f"{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            )
        elif type(current) == Kraken:
            type_write("The Kraken stirs in the deep below you.")
            choices = (
                f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}interact{BOLD_END}/"
                f"{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            )
        elif type(current) == DemonsPalace:
            type_write("The Demon's Palace stands before you, its gates scorched black.")
            choices = (
                f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}interact{BOLD_END}/"
                f"{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            )
        elif type(current) == Room:
            key_room = current
            if key_room.key:
                type_write(f"You are at a locked room. You need a {key_room.key_type} to proceed.")
                choices = (
                    f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                    f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}use {key_room.key_type}{BOLD_END}/"
                    f"{BOLD_START}search{BOLD_END}/{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
                )
            else:
                choices = (
                    f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                    f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/"
                    f"{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
                )
        else:
            choices = (
                f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
                f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}search{BOLD_END}/"
                f"{BOLD_START}eat{BOLD_END}/{BOLD_START}exit island{BOLD_END})"
            )

        return current

    def handle_riddle_failure():
        """Increment failed riddle counter and return 'riddle_failure' if limit reached."""
        failed = player_name.add_failed_riddle_attempt()
        if failed >= 3:
            return "riddle_failure"
        return None

    current = refresh_location_state()

    # Main island exploration loop
    while True:
        menu_choice = type_write(
            "What would you like to do?\n" + choices,
            userin=True,
        )
        clear()

        if menu_choice.startswith("move"):
            alive = player_name.move()
            if not alive:
                # Player starved — prompt to quit or restart
                type_write("You collapse from starvation... Einstein finds you.\n")
                type_write("GAME OVER: You starved to death!\n")
                while True:
                    game_choice = type_write(
                        "Would you like to quit or restart?\n"
                        + f"({BOLD_START}quit{BOLD_END}/{BOLD_START}restart{BOLD_END})",
                        userin=True,
                    )
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
                # Search inventory for the required key item
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
                    # Dryad requires a Magical Branch as tribute before attempting the riddle
                    has_branch = any("Magical Branch" in item[0] for item in player_name.jacket.inventory)
                    if has_branch:
                        type_write("You offer the Magical Branch. The Dryad accepts it and regards you with ancient eyes.\n")
                        if current.attempt_riddle(type_write, BOLD_START, BOLD_END):
                            # Consume the branch on success
                            for item in player_name.jacket.inventory:
                                if "Magical Branch" in item[0]:
                                    item[0] = item[0].split(". ")[0] + ". EMPTY"
                                    break
                            player_name.level_up()
                            player_name.reset_failed_riddle_attempts()
                        else:
                            type_write("The Dryad rejects your magical branch.\n")
                            result = handle_riddle_failure()
                            if result:
                                return result
                    else:
                        type_write(
                            "The Dryad stares at you coldly.\n"
                            "\"Bring me a Magical Branch as tribute before I will speak with you.\"\n"
                        )
                else:
                    type_write("The Dryad nods at you slowly. You have already proven yourself.\n")

            elif type(current) == Kraken:
                if not current.riddle_solved:
                    if current.attempt_riddle(type_write, BOLD_START, BOLD_END):
                        player_name.level_up()
                        player_name.reset_failed_riddle_attempts()
                    else:
                        result = handle_riddle_failure()
                        if result:
                            return result
                else:
                    type_write("The Kraken's eye slides toward you. It has already deemed you worthy.\n")

            elif type(current) == DemonsPalace:
                if not current.riddle_solved:
                    # Demon's Palace requires the Eye of Hell as an offering
                    has_eye = any("Eye of Hell" in item[0] for item in player_name.jacket.inventory)
                    if has_eye:
                        type_write("You hold out the Eye of Hell. The palace gates shudder and groan open...\n")
                        if current.attempt_riddle(type_write, BOLD_START, BOLD_END):
                            # Consume the Eye of Hell on success
                            for item in player_name.jacket.inventory:
                                if "Eye of Hell" in item[0]:
                                    item[0] = item[0].split(". ")[0] + ". EMPTY"
                                    break
                            player_name.reset_failed_riddle_attempts()
                            type_write(
                                "\nYou have escaped back to the real world but you can't find anyone alive around you,\n"
                                "the world seems to be empty and you are the last human being alive......\n"
                            )
                            return "game_completed"
                        else:
                            type_write("The demons reject your offering. The Eye of Hell remains with you.\n")
                            result = handle_riddle_failure()
                            if result:
                                return result
                    else:
                        type_write(
                            "The palace gates do not move. Something is missing...\n"
                            "\"Bring us the Eye of Hell.\"\n"
                        )
                else:
                    type_write("The demons watch you in silence. You have already passed their test.\n")

            else:
                type_write("There is nothing to interact with here.\n")

        elif menu_choice.startswith("search"):
            current = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            if type(current) == Inventory:
                loot_stash = current
                loot_stash.view_inventory()
                item_choice = type_write(
                    "What would you like to withdraw?\n"
                    + f"({', '.join([str(i + 1) for i in range(len(loot_stash.inventory))])})",
                    userin=True,
                )
                loot_stolen = False
                if item_choice in [str(i + 1) for i in range(len(loot_stash.inventory))]:
                    for i in range(len(player_name.jacket.inventory)):
                        if player_name.jacket.inventory[i][0][-5:] == "EMPTY":
                            item_label = loot_stash.inventory[int(item_choice) - 1][0].split(". ")[1]
                            if item_label != "EMPTY" and item_label != "Pocket":
                                # Pick up a regular item into an empty slot
                                player_name.jacket.inventory[i][0] = f"{i + 1}. {item_label}"
                                type_write("Item successfully picked up!\n")
                            elif item_label == "Pocket":
                                # Pocket adds an extra inventory slot to the jacket
                                type_write("Pocket added to jacket.\n")
                                player_name.jacket.inventory.append(
                                    [f"{len(player_name.jacket.inventory) + 1}. EMPTY"]
                                )
                            else:
                                type_write("There's nothing to pick up. \n")
                            loot_stash.inventory[int(item_choice) - 1][0] = f"{item_choice}. EMPTY"
                            loot_stolen = True
                            break
                    if not loot_stolen:
                        type_write("It appears your pockets are full!\n")
            else:
                type_write("There is no loot stash here.\n")

        elif menu_choice.startswith("eat"):
            # Collect all food items currently in the player's inventory
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
                    type_write(f"{food}")
                food_choice = type_write("Choose an option: ", userin=True)

                if food_choice in [str(i + 1) for i in range(len(food_items))]:
                    chosen_idx = int(food_choice) - 1
                    item_idx, food_name = food_items[chosen_idx]
                    food_type = food_name.split(". ")[1]
                    success, restore_amount = player_name.hunger.eat(food_type)
                    if success:
                        type_write(f"You eat the {food_type} and restore {restore_amount} hunger points!\n")
                        # Remove the consumed food from inventory
                        player_name.jacket.inventory[item_idx][0] = f"{item_idx + 1}. EMPTY"
                    else:
                        type_write("You cannot eat that!\n")
                else:
                    type_write("Invalid choice!\n")

        elif menu_choice.startswith("exit"):
            # Only allow exit from a valid entrance/exit tile
            for i in player_name.map_choice.start_pos:
                # print(i.split(","))
                if player_name.pos == [int(i.split(",")[0]), int(i.split(",")[1])]:
                    player_name.map_choice = main_map
                    player_name.pos = original_position
                    type_write(
                        f"You have exited the {main_map.plot[player_name.pos[0]][player_name.pos[1]]} successfully!\n"
                    )
                    return

            type_write("You need to be at an entrance/exit first!\n")

        else:
            type_write("You cannot do that!\n")

        current = refresh_location_state()


def main():
    """Main game loop — handles player selection and top-level menu."""

    # Player selection screen
    while True:
        player_name = type_write(
            f"Who would you like your player to be?\n({BOLD_START}Steve{BOLD_END})",
            userin=True,
        )
        if player_name.lower().startswith("steve"):
            player_name = steve
            break
        else:
            clear()
            type_write("That player doesn't exist!")

    clear()
    type_write(f"Hello {player_name.name.capitalize()}~")
    run_start_time = datetime.now()

    # Main game loop
    while True:

        # Unlock islands as the player levels up
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

        menu_choice = type_write(
            "What would you like to do?\n"
            + f"({BOLD_START}move{BOLD_END}/{BOLD_START}view map{BOLD_END}/"
            f"{BOLD_START}inspect jacket{BOLD_END}/{BOLD_START}eat{BOLD_END}/"
            f"{BOLD_START}enter island{BOLD_END}/{BOLD_START}quit{BOLD_END})",
            userin=True,
        )

        if menu_choice == "quit":
            log_run(player_name, run_start_time, "Quit")
            type_write(f"\nGood bye, {player_name.name.capitalize()}...")
            break

        clear()

        if menu_choice.startswith("view"):
            player_name.map_choice.view_plot()

        elif menu_choice.startswith("eat"):
            type_write(player_name.hunger.get_status())

            # Collect all food items currently in the player's inventory
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
                    type_write(f"{i + 1}. {food}")
                food_choice = type_write("Choose an option: ", userin=True)

                if food_choice in [str(i + 1) for i in range(len(food_items))]:
                    chosen_idx = int(food_choice) - 1
                    item_idx, food_name = food_items[chosen_idx]
                    food_type = food_name.split(". ")[1]
                    success, restore_amount = player_name.hunger.eat(food_type)
                    if success:
                        type_write(f"You eat the {food_type} and restore {restore_amount} hunger points!\n")
                        # Remove the consumed food from inventory
                        player_name.jacket.inventory[item_idx][0] = f"{item_idx + 1}. EMPTY"
                    else:
                        type_write("You cannot eat that!\n")
                else:
                    type_write("Invalid choice!\n")

        elif menu_choice.startswith("move"):
            alive = player_name.move()
            if not alive:
                # Player starved — prompt to quit or restart
                type_write("You collapse from starvation... Einstein finds you.\n")
                type_write("GAME OVER: You starved to death!\n")
                while True:
                    game_choice = type_write(
                        "Would you like to quit or restart?\n"
                        + f"({BOLD_START}quit{BOLD_END}/{BOLD_START}restart{BOLD_END})",
                        userin=True,
                    )
                    if game_choice.lower().startswith("quit"):
                        log_run(player_name, run_start_time, "Starved to Death")
                        type_write(f"\nGood bye, {player_name.name.capitalize()}...")
                        return
                    elif game_choice.lower().startswith("restart"):
                        log_run(player_name, run_start_time, "Starved to Death")
                        reset_game(player_name)
                        run_start_time = datetime.now()
                        break
                    clear()
                    type_write("Invalid choice!\n")

        elif menu_choice.startswith("enter"):
            result = explore_island(player_name)
            if result == "game_over":
                log_run(player_name, run_start_time, "Starved to Death")
                break
            elif result == "restart":
                log_run(player_name, run_start_time, "Starved to Death")
                reset_game(player_name)
                run_start_time = datetime.now()
            elif result == "game_completed":
                log_run(player_name, run_start_time, "Game Completed")
                break
            elif result == "riddle_failure":
                # Player failed too many riddles — prompt to quit or restart
                type_write("You have failed too many riddles in a row.\n")
                type_write("Einstein catches you and ends your journey.\n")
                while True:
                    game_choice = type_write(
                        "Would you like to quit or restart?\n"
                        + f"({BOLD_START}quit{BOLD_END}/{BOLD_START}restart{BOLD_END})",
                        userin=True,
                    )
                    if game_choice.lower().startswith("quit"):
                        log_run(player_name, run_start_time, "Riddle Failure")
                        type_write(f"\nGood bye, {player_name.name.capitalize()}...")
                        return
                    elif game_choice.lower().startswith("restart"):
                        log_run(player_name, run_start_time, "Riddle Failure")
                        reset_game(player_name)
                        run_start_time = datetime.now()
                        break
                    clear()
                    type_write("Invalid choice!\n")

        elif menu_choice.startswith("inspect"):
            player_name.jacket.view_inventory()

        else:
            type_write("You cannot do that!")

        # Check if the player is standing on a locked room and prompt to use the key
        if type(player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]) == Room:
            key_room = player_name.map_choice.plot[player_name.pos[0]][player_name.pos[1]]
            if key_room.key:
                type_write(f"You need a {key_room.key_type} to proceed.")
                ask_key = type_write(
                    f"Use {key_room.key_type}?\n({BOLD_START}Y{BOLD_END}/{BOLD_START}N{BOLD_END})",
                    userin=True,
                )
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