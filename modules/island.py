import tabulate
from plot import Plot

class Island:
    
    def __init__(self, name, start_pos, plot, description):
        self.name = name
        self.start_pos = start_pos
        self.plot = Plot(self.name, plot, self.start_pos)
        self.description = description

    
    def __str__(self):
        return self.name

    def view_island(self):
        return tabulate.tabulate(self.plot, tablefmt="fancy_grid") + "\n"