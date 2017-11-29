import numpy as np

materials = {"brick": 0.1, "airbrick": 0.2}


class Wall:
    def __init__(self, material, vector_coord):
        self.material = material
        self.vector_coord = vector_coord
        self.alpha = materials[material]

    def get_jamming(self, point):
        pass


class Building:
    def __init__(self, walls_vector):
        self.walls_vector = walls_vector

    def jamming(self, point):
        pass
