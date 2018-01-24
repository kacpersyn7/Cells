from input_output import *
from pso import *
from targetfunc import *

if __name__ == "main":
    people = read_people_from_file("kolka_i_kwadraty", g.ROWS, g.COLS)
    files_with_people = ["studnia_potencjalu.txt", "kolka_i_kwadraty", "Plik_z_kolkami", "kolka_i_kwadraty_z_szumem"]
    population = [100, 200, 500, 1000]
    my_func = Target(people)
    i = 0
    counter = 16 * 3
    print("Sztartuuuuje")
    start_time = time.time()
    for files in files_with_people:
        for quanity in population:
            for i in range(3):
                people = read_people_from_file(files, g.ROWS, g.COLS)
                my_func = Target(people)
                out = pso(my_func, 0, 1250, quanity, 1, 1, 1, 2500)
                counter = counter - 1
                print("Jeszcze tylko: ", counter)
                write2file_out(out, i, files, quanity)  # generuje 16*3 plików XDDDDDD
    diff = time.time() - start_time
    diff = diff / 60
    print("Test trwał: ", diff, " minut")
    it, tf = read_from_file_it_targ("iterate_target_func_kolka_i_kwadraty_z_szumem_0_200")
    it1, tf1 = read_from_file_it_targ("iterate_target_func_kolka_i_kwadraty_z_szumem_0_500")
    it2, tf2 = read_from_file_it_targ("iterate_target_func_kolka_i_kwadraty_z_szumem_2_1000")

    heatmap = read_people_from_file("kolka_i_kwadraty_z_szumem", g.COLS, g.ROWS)
    result1 = read_people_from_file("outbitmapa_router_1_kolka_i_kwadraty_z_szumem_0_500 0", g.COLS, g.ROWS)
    result2 = read_people_from_file("outbitmapa_router_2_kolka_i_kwadraty_z_szumem_0_500 0", g.COLS, g.ROWS)
