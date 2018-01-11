import numpy as np
import numba
import globals as g



@numba.jit(nopython=True, cache=True)
#@numba.vectorize([numba.types.Array(numba.float64,2,'C')(numba.types.Array(numba.float64,2,'C'),numba.int64,numba.types.Array(numba.float64,2,'C'),numba.int64,numba.int64,numba.types.Array(numba.float64,2,'C'))])
def update_result_area_outer(ap_bitmap,radius,result_area,x_size,y_size,circle):
    access_points = np.where(ap_bitmap == 1)
    for x, y in zip(access_points[0], access_points[1]):
        diff_x = radius - x
        diff_y = radius - y
        diff_x_2 = -diff_x
        diff_y_2 = -diff_y
        if diff_x < 0:
            diff_x = 0
        else:
            diff_x_2 = 0
        if diff_y < 0:
            diff_y = 0
        else:
            diff_y_2 = 0

        result_area[diff_x_2:(x + radius + 1), diff_y_2:(y + radius + 1)] = np.maximum(
            result_area[diff_x_2:(x + radius + 1), diff_y_2:(y + radius + 1)],
            (circle[diff_x:(radius + x_size - x), diff_y:(radius + y_size - y)]))
    return result_area


class AccessPoint:
    def __init__(self, cost=100, max_power=10, radius=16, access_area_fun=lambda point: point[0] ** 2 + point[1] ** 2,
                 x_size=g.COLS,
                 y_size=g.ROWS):
        self.max_power = max_power
        self.access_area_fun = access_area_fun
        self.cost = cost
        self.x_size = x_size
        self.y_size = y_size
        self.radius = radius
        self.circle = np.copy(access_area_fun(np.ogrid[-radius:(radius + 1), -radius:(radius + 1)]))
        self.circle[self.circle > radius ** 2] = -2
        self.circle = (1. / (self.circle + 0.5)) * self.max_power
        self.circle[self.circle < 0] = 0

    def update_result_area(self, ap_bitmap, result_area):
        result_area = update_result_area_outer(ap_bitmap, self.radius, result_area, self.x_size, self.y_size, self.circle)
        return result_area

    """def update_result_area(self, ap_bitmap, result_area):
        access_points = np.where(ap_bitmap == 1)
        for x, y in zip(access_points[0], access_points[1]):
            diff_x = self.radius - x
            diff_y = self.radius - y
            diff_x_2 = -diff_x
            diff_y_2 = -diff_y
            if diff_x < 0:
                diff_x = 0
            else:
                diff_x_2 = 0
            if diff_y < 0:
                diff_y = 0
            else:
                diff_y_2 = 0

            result_area[diff_x_2:(x + self.radius + 1), diff_y_2:(y + self.radius + 1)] = np.maximum(
                result_area[diff_x_2:(x + self.radius + 1), diff_y_2:(y + self.radius + 1)],
                (self.circle[diff_x:(self.radius + self.x_size - x), diff_y:(self.radius + self.y_size - y)]))
        return result_area"""
