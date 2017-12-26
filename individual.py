import globals as g
from accesspoint import *


##For more than one type of accesspoint

class Individual:
    def __init__(self, dimension=0, x_size=g.COLS, y_size=g.ROWS):
        self.result_area = Area(x_size, y_size)
        self.dimension = dimension
        if (dimension > 0):
            self.bitmap = np.zeros((x_size, y_size, dimension))

    def target_function(self):
        pass

    def generate_first_individual(self, probability):
        pass
