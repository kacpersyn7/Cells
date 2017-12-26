from area import Area
from globals import *


class UserEquipment:
    def __init__(self, max_request, x_size=COLS, y_size=ROWS):
        self.area = Area(x_size, y_size)
        self.max_request = max_request

    def get_random(self):
        return self.area.generate_random(self.max_request)
