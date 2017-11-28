import numpy as np
import space as hp


class Router:
    users = np.array([])

    def __init__(self, x_coord, y_coord, max_power, name, max_range, users):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.max_power = max_power
        self.name = name
        self.max_range = max_range
        self.users = users
        return self

    def get_power(self, person):
        distance = hp.distance_between_two_points(self, person)
        if distance < self.max_range:
            return 1 / (distance * distance)
        else:
            return 0
