import numpy as np
import math

def distance_between_rou_pers(router, person):
    diff_x = router.x_coord - person.x_coord
    diff_y = router.y_coord - person.y_coord
    return math.sqrt(abs(diff_x*diff_x + diff_y*diff_y))