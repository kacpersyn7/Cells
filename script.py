import matplotlib.pyplot as plt

from pso import *
from targetfunc import *

people = np.zeros((g.COLS, g.ROWS))
people[10][10] = 40
#people[40][40] = 40
my_func = Target(people)
best_bitmap, best_value = pso(my_func, 0, 900, 800, 1, 1, 1, 1000)

x, y = np.where(best_bitmap[1] == 1)

plt.plot(x, y, 'ro')
plt.axis([0, 49, 0, 49])
plt.show()
