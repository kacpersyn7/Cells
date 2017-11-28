import numpy as np

materials = {"brick": 0.1, "airbrick": 0.2 }


class Wall:
    def __init__(self, material, vector_coord):
        self.material = material
        self.vector_coord = vector_coord


class Building:
    walls = np.array([])

    def __init__(self, walls, material):
        self.walls = walls
        self.material = material
