import tabulate
from modules.type_write import *

class Plot:
    def __init__(self, name: str, plot: str, start_pos: str, end_pos: str = None):
        self.name = name
        self.plot = [["" for _ in range(int(plot.split("x")[0]))] \
                     for _ in range(int(plot.split("x")[1]))]
        self.start_pos = start_pos
        self.end_pos = end_pos


    def __str__(self):
        return self.name

    def view_plot(self):
        type_write("- THE MAP")
        print(tabulate.tabulate(self.plot, tablefmt="fancy_grid"))


class Island(Plot):
    def __init__(self, name, plot, start_pos, description: str, end_pos=None):
        super().__init__(name, plot, start_pos, end_pos)
        self.description = description
