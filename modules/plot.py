import tabulate
from modules.type_write import *


class Plot:
    """Represents a 2D grid map that can be displayed as a table."""

    def __init__(self, name: str, plot: str, start_pos: list):
        self.name = name          # Display name of the map
        self.start_pos = start_pos  # List of valid start positions as "row,col" strings
        # Build a 2D grid from the "colsxrows" format string (e.g. "3x2")
        self.plot = [
            ["" for _ in range(int(plot.split("x")[0]))]
            for _ in range(int(plot.split("x")[1]))
        ]

    def __str__(self):
        return self.name

    def view_plot(self):
        """Display the map grid as a formatted table."""
        type_write("- THE MAP")
        print(tabulate.tabulate(self.plot, tablefmt="fancy_grid"))


class Island(Plot):
    """A named region of the world with its own grid map and description."""

    def __init__(self, name: str, plot: str, start_pos: list, description: str):
        super().__init__(name, plot, start_pos)
        self.description = description  # Flavour text shown when the player enters the island