import numpy as np
from scipy import optimize
from pyswarm import pso


class Area:

    x_size = 0
    y_size = 0

    def __init__(self, x_size, y_size, alpha, space_cord, walls_vector, people_vector):
        self.x_size = x_size
        self.y_size = y_size
        self.space_cord = space_cord
        self.wall_coord = walls_vector
        self.people_coord = people_vector

    def cells_conditions(self):
        pass


# numpy matrix with coords of walls
# numpy matrix with coords of cells
# numpy matrix with coords of people
# numpy matrix with values of every area point
# conditions for cells coords
# idea - import from bitmap file
def update_value(area, cells_coord):
    pass
