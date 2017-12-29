import numpy as np

import globals as g
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

    def update_result_area(self, access_area_fun, get_power, dim):
        access_points = np.where(self.ap_bitmap[dim] == 1)
        new_result_area = np.copy(self.result_area)
        for x, y in zip(access_points[0], access_points[1]):
            temp_y, temp_x = np.ogrid[-x:self.x_size - x, -y:self.y_size - y]
            mask_indexes = np.where(access_area_fun(temp_x, temp_y))
            new_result_area[mask_indexes] = get_power(x, y, mask_indexes[0], mask_indexes[1])
            diff = np.where((new_result_area - self.result_area) < 0)
            new_result_area[diff] = self.result_area[diff]
            self.result_area = np.copy(new_result_area)
        
    def target_function(self):
        pass
