from particle import *
from targetfunc import *
from pso import *
people = np.zeros((g.COLS, g.ROWS))
people[10][10] = 40
my_func = Target(people)
best_bitmap, best_value = pso(my_func, 0, 390)