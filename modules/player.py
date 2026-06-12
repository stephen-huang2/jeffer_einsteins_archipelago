from modules.clear import clear
from modules.plot import *
from modules.type_write import *
from modules.inventory import *
from modules.hunger import Hunger


class Player:
    """Represents the player character, tracking position, hunger, and progress."""

    def __init__(
        self,
        name: str,
        pos: list,
        map_choice: Plot,
        jacket: Inventory,
        level: int = 0,
    ):
        self.name = name                    # Player's display name
        self.pos = pos                      # Current [row, col] position on the map
        self.map_choice = map_choice        # The map/island the player is currently on
        self.jacket = jacket                # Player's inventory (their jacket)
        self.level = level                  # Current level, used to unlock new islands
        self.hunger = Hunger()              # Hunger tracker instance
        self.failed_riddle_attempts = 0     # Counter for consecutive failed riddles

    def __str__(self):
        return self.name

    def add_failed_riddle_attempt(self):
        """Increment the failed riddle counter and return the new total."""
        self.failed_riddle_attempts += 1
        return self.failed_riddle_attempts

    def reset_failed_riddle_attempts(self):
        """Reset the failed riddle counter to zero after a success."""
        self.failed_riddle_attempts = 0

    def move(self):
        """
        Interactive movement loop. Prompts the player for a direction each step.
        Depletes hunger on each move. Returns False if the player starves, True otherwise.
        """
        while True:
            # Display the current tile name if it exists
            if self.map_choice.plot[self.pos[0]][self.pos[1]] != "":
                type_write(
                    f"You are at "
                    f"{self.map_choice.plot[self.pos[0]][self.pos[1]]}."
                )
            else:
                type_write("There's nothing here.")

            type_write(self.hunger.get_status())
            move_choice = type_write(
                f"Where would you like to move?\n"
                f"({BOLD_START}up{BOLD_END}/"
                f"{BOLD_START}down{BOLD_END}/"
                f"{BOLD_START}left{BOLD_END}/"
                f"{BOLD_START}right{BOLD_END}/"
                f"{BOLD_START}stop{BOLD_END})",
                userin=True,
            )
            clear()

            if move_choice == "up" and self.pos[0] > 0:
                self.pos[0] -= 1
                if not self.hunger.deplete(1):
                    return False
                continue

            elif move_choice == "down" and self.pos[0] < len(self.map_choice.plot) - 1:
                self.pos[0] += 1
                if not self.hunger.deplete(1):
                    return False
                continue

            elif move_choice == "left" and self.pos[1] > 0:
                self.pos[1] -= 1
                if not self.hunger.deplete(1):
                    return False
                continue

            elif move_choice == "right" and self.pos[1] < len(self.map_choice.plot[0]) - 1:
                self.pos[1] += 1
                if not self.hunger.deplete(1):
                    return False
                continue

            elif move_choice == "stop":
                break

            # Handle invalid input or out-of-bounds movement attempts
            clear()
            if move_choice in ["up", "down", "left", "right"]:
                type_write("You are at the edge of the map! ", newline=False)
            else:
                type_write("That's not a valid direction! ", newline=False)

        return True

    def level_up(self):
        """Increment the player's level, unlocking the next island on the main map."""
        self.level += 1