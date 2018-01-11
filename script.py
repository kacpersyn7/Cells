from pso import *
from targetfunc import *

people = np.zeros((g.COLS, g.ROWS))
people[10][10] = 40
#people[40][40] = 40
my_func = Target(people)
best_bitmap, best_value = pso(my_func, 0, 900, 200, 1, 1, 1, 5000)
