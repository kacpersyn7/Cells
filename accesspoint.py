import numpy as np


class AccessPoint:
    def __init__(self, cost=100, max_power=10, access_area_fun=lambda x, y: x * x + y * y <= 16,
                 dist_fun=lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float)):
        self.max_power = max_power
        self.access_area_fun = access_area_fun
        self.dist_fun = dist_fun
        self.cost = cost

    def get_power(self, ap_x, ap_y, ue_x, ue_y):
        distance = self.dist_fun(ue_x - ap_x, ue_y - ap_y)
        distance[np.where(distance == 0)[0]] = 0.5
        return (1. / distance) * self.max_power
