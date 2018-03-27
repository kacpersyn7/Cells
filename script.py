from pso import pso
from input_output import read_people_from_file
import time
from targetfunc import Target
import graphics
import numpy as np
import globals as g

if __name__ == "__main__":
    people = read_people_from_file("kolka_i_kwadraty", g.ROWS, g.COLS)
    population = [100, 200, 500, 1000]
    my_func = Target(people)
    out = pso(my_func, 0, 100, 200, 1, 1, 1, 1000)
    iterated, best_bitmap, target_f = zip(*out)
    heatmap = my_func.get_result_area(best_bitmap[-1])
    x, y = np.where(best_bitmap[-1][1] == 1)
    start_time2137 = time.time()
    print("Calosc wykonywala sie: ", time.time() - start_time2137)
    graphics.show_and_save_target_function(iterated, target_f)
    graphics.show_and_save_accesspoints(best_bitmap[-1])
    graphics.show_and_save_power(people, heatmap)
