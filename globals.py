import numpy as np
from numba import jit,vectorize
COLS = 200
ROWS = 200

access_points_types = [{'cost': 100, 'max_power': 100, 'radius': 3},

                       {'cost': 213, 'max_power': 120, 'radius': 4}
                       ]
#@vectorize(nopython = True, target = 'cpu')
@jit(nopython=True, parallel=True)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
