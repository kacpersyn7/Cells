import numpy as np

import globals as g


class AccessPoint:
    def __init__(self, cost=100, max_power=10, access_area_fun=lambda x, y: x * x + y * y <= 16,
                 dist_fun=lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float), x_size=g.COLS,
                 y_size=g.ROWS):
        self.max_power = max_power
        self.access_area_fun = access_area_fun
        self.dist_fun = dist_fun
        self.cost = cost
        self.x_size = x_size
        self.y_size = y_size

    def get_power(self, ap_x, ap_y, ue_x, ue_y):
        distance = self.dist_fun(ue_x - ap_x, ue_y - ap_y)
        distance[np.where(distance == 0)[0]] = 0.5
        return (1. / distance) * self.max_power

    def update_result_area(self, ap_bitmap, result_area):
        access_points = np.where(ap_bitmap == 1)
        new_result_area = np.copy(result_area)
        for x, y in zip(access_points[0], access_points[1]):
            temp_y, temp_x = np.ogrid[-x:self.x_size - x, -y:self.y_size - y]
            mask_indexes = np.where(self.access_area_fun(temp_x, temp_y))
            new_result_area[mask_indexes] = self.get_power(x, y, mask_indexes[0], mask_indexes[1])
            diff = np.where((new_result_area - result_area) < 0)
            new_result_area[diff] = result_area[diff]
            result_area = np.copy(new_result_area)
