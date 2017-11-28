import numpy as np
import math


def distance_between_two_points(first, second):
    diff_x = first.x_coord - second.x_coord
    diff_y = first.y_coord - second.y_coord
    return math.sqrt(abs(diff_x * diff_x + diff_y * diff_y))
