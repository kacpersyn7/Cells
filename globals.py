import numpy as np

COLS = 20
ROWS = 20

access_points_types = [{'cost': 100, 'max_power': 100, 'access_area_fun': lambda x,
                                                                                 y: x * x + y * y <= 9,
                        'dist_fun': lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float)},

                       {'cost': 213, 'max_power': 120, 'access_area_fun': lambda x,
                                                                                 y: x * x + y * y <= 16,
                        'dist_fun': lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float)}
                       ]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
