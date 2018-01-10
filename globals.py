import numpy as np

COLS = 50
ROWS = 50

access_points_types = [{'cost': 100, 'max_power': 100, 'radius': 3},

                       {'cost': 213, 'max_power': 120, 'radius': 4}
                       ]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
