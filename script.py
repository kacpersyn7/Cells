from pso import *
from targetfunc import *

people = np.zeros((g.COLS, g.ROWS))
people[10][10] = 40
my_func = Target(people)
best_bitmap, best_value = pso(my_func, 0, 9000, 500, 1.5, 0.5, 1, 5000)
