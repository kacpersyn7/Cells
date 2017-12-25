import numpy as np


class Area:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.area = np.zeros((x_size, y_size))  # unnecessary, I think, or not

    def generate_random(self, max_request):
        self.area = np.random.randint(0, max_request, size=(self.x_size, self.y_size))
        return self.area
