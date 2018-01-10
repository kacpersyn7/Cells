import numpy as np

import globals as g


class AccessPoint:
    def __init__(self, cost=100, max_power=10, radius=16, access_area_fun=lambda point: point[0] ** 2 + point[1] ** 2,
                 dist_fun=lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float), x_size=g.COLS,
                 y_size=g.ROWS):
        self.max_power = max_power
        self.access_area_fun = access_area_fun
        self.dist_fun = dist_fun
        self.cost = cost
        self.x_size = x_size
        self.y_size = y_size
        self.radius = radius
        self.circle = np.copy(access_area_fun(np.ogrid[-radius:(radius + 1), -radius:(radius + 1)]))
        self.circle[self.circle > radius ** 2] = -2
        self.circle = (1. / (self.circle + 0.5)) * self.max_power
        self.circle[self.circle < 0] = 0

    def get_power(self, ap_x, ap_y, ue_x, ue_y):
        distance = self.dist_fun(ue_x - ap_x, ue_y - ap_y)
        distance[np.where(distance == 0)[0]] = 0.5
        return (1. / distance) * self.max_power

    def update_result_area(self, ap_bitmap, result_area):
        access_points = np.where(ap_bitmap == 1)
        new_result_area = np.copy(result_area)
        # mozna sie obejsc bez kopiowania chyba
        for x, y in zip(access_points[0], access_points[1]):
            diff_x = self.radius - x
            diff_y = self.radius - y
            if (diff_x < 0):
                diff_x = 0
            if (diff_y < 0):
                diff_y = 0
            diff_x_2 = x - self.radius
            diff_y_2 = y - self.radius
            if (diff_x_2 < 0):
                diff_x_2 = 0
            if (diff_y_2 < 0):
                diff_y_2 = 0
            new_result_area[diff_x_2:(x + self.radius + 1), diff_y_2:(y + self.radius + 1)] = np.maximum(
                new_result_area[diff_x_2:(x + self.radius + 1), diff_y_2:(y + self.radius + 1)],
                (self.circle[diff_x:(self.radius + self.x_size - x), diff_y:(self.radius + self.y_size - y)]))
            diff = np.where((new_result_area - result_area) < 0)
            new_result_area[diff] = result_area[diff]
        return new_result_area
