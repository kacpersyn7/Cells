import matplotlib.pyplot as plt

from input_output import *
from pso import *
from targetfunc import *

if __name__ == "__main__":
    people = read_people_from_file("kolka_i_kwadraty", g.ROWS, g.COLS)
    population = [100, 200, 500, 1000]
    my_func = Target(people)
    out = pso(my_func, 0, 100, 200, 1, 1, 1, 2000)
    iterated, best_bitmap, target_f = zip(*out)
    x, y = np.where(best_bitmap[-1][1] == 1)
    start_time2137 = time.time()
    print("Calosc wykonywala sie: ", time.time() - start_time2137)
    x, y = np.where(best_bitmap[-1][1] == 1)
    print(x)
    print(y)
    # write2file(x,y)
    plt.plot(iterated, target_f, 'ro')
    plt.show()
    plt.plot(x, y, 'ro')
    plt.axis([0, g.COLS - 1, 0, g.ROWS - 1])
    x, y = np.where(best_bitmap[-1][0] == 1)
    plt.plot(x, y, 'bx'
                   '')
    plt.axis([0, g.COLS - 1, 0, g.ROWS - 1])
    plt.show()

    plt.show()
