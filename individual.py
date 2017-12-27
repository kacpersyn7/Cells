from accesspoint import *


##For more than one type of accesspoint

class Individual:
    def __init__(self, access_points_types=g.access_points_types, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.result_area = np.zeros((x_size, y_size))
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]

    def target_function(self):
        pass

    def generate_first_individual(self, probability):
        pass
