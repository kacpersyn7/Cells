from pso import *
from targetfunc import *

if __name__ == "__main__":
    resolution = (50, 50)
    people1 = np.zeros(resolution)
    people1[20][20] = 1
    access_points_types = [
        {'cost': 100, 'max_power': 100, 'radius': 3, 'access_area_fun': lambda point: point[0] ** 2 + point[1] ** 2},

        {'cost': 213, 'max_power': 120, 'radius': 4, 'access_area_fun': lambda point: point[0] ** 2 + point[1] ** 2},

    ]

    fc1 = Target(people1, access_points_types)
    g_bitmap, g_target = pso(fc1)
