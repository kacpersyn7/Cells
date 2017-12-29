from accesspoint import *


##For more than one type of accesspoint

class Individual:
    def __init__(self, dimension, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.result_area = np.zeros((x_size, y_size))
        self.ap_bitmap = np.zeros((dimension, x_size, y_size))
        self.dimension = dimension
        # self.access_points = [AccessPoint(**x) for x in access_points_types]

    def generate_first_individual(self, probability):
        for i in range(self.dimension):
            self.ap_bitmap[i] = np.logical_not(
                np.logical_or(np.random.randint(0, probability[i], size=(self.x_size, self.y_size)), 0)).astype(int)

    def target_function(self):
        pass
