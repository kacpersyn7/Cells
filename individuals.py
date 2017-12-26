import globals as g


class Individuals:
    def __init__(self, population_size, dimension=0, x_size=g.COLS, y_size=g.ROWS):
        self.population_size = population_size
        self.dimension = dimension
