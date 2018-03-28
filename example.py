from pso import pso
from input_output import read_people_from_file
import time
from targetfunc import Target
import graphics

if __name__ == "__main__":
    people = read_people_from_file("kolka_i_kwadraty", 50, 50)
    my_func = Target(people)
    start_time2137 = time.time()
    out = pso(my_func, 0, 476, 200, 1, 1, 1, 1000)
    print("Calosc wykonywala sie: ", time.time() - start_time2137)
    iterated, best_bitmap, target_f = zip(*out)
    heatmap = my_func.get_result_area(best_bitmap[-1])
    graphics.show_and_save_target_function(iterated, target_f)
    graphics.show_and_save_accesspoints(best_bitmap[-1])
    graphics.show_and_save_power(people, heatmap)