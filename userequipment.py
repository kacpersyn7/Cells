import numpy as np

import globals as g


class UserEquipment:
    def __init__(self, max_request, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.area = np.zeros((x_size, y_size))
        return self

    def get_random(self):
        self.area = np.random.randint(0, self.max_request, size=(self.x_size, self.y_size))
