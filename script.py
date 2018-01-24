import matplotlib.pyplot as plt

from pso import *
from targetfunc import *


def read_people_from_file(name, rows, cols):
    """ Czyta bitmape ludzi z pliku, jako argument przyjmuje nazwe pliku i zwraca zczytaną bitmapę"""
    people_heatmap = np.zeros((rows, cols))
    with open(name, 'r') as file:
        for line in file:
            parse = line.split()
            coords = []
            for char in parse:
                if char.isnumeric():
                    coords.append(int(char))
            # print(coords)
            if coords[0] < cols:
                if coords[1] < rows:
                    power = coords[-1]
                    people_heatmap[coords[0]][coords[1]] = power
    return people_heatmap


def write2file(num_array, name, index):
    x,y = np.where(num_array > 0)
    string2 = "out" + name + " " + str(index)
    with open(string2, 'w') as file:
        for i in range(len(x)):
            string = "x: " + str(x[i]) + " y: " + str(y[i]) + " power: " + str(int(num_array[x[i]][y[i]])) + "\n"
            file.write(string)

def write2file_out(out, index, people_f_name, population):
    iterated, best_bitmap, target_f = zip(*out)
    string = "bitmapa_router_1_" + people_f_name + "_" + str(index) + "_" + str(population)
    write2file(best_bitmap[-1][0], string,index)
    string = "bitmapa_router_2_" + people_f_name + "_" + str(index) + "_" + str(population)
    write2file(best_bitmap[-1][1], string, index)
    string = "iterate_target_func_" + people_f_name + "_" + str(index) + "_" + str(population)
    with open(string, 'w') as file:
        for it in range(len(iterated)):
            string2 = "iterate " + str(iterated[it]) + " tarrget_func: " + str(target_f[it]) +  "\n"
            file.write(string2)

if __name__ == "__main__":
    people = read_people_from_file("kolka_i_kwadraty", g.ROWS, g.COLS)

    files_with_people=["studnia_potencjalu.txt", "kolka_i_kwadraty", "Plik_z_kolkami", "kolka_i_kwadraty_z_szumem"]
    population = [100, 200, 500, 1000]
    my_func = Target(people)
    i = 0
    counter = 16*3
    print("Sztartuuuuje")
    #
    # out = pso(my_func, 0, 100, 200, 1, 1, 1, 2000)
    # iterated, best_bitmap, target_f = zip(*out)
    start_time = time.time()
    for files in files_with_people:
        for quanity in population:
            for i in range(3):
                people = read_people_from_file(files, g.ROWS, g.COLS)
                my_func = Target(people)
                out = pso(my_func, 0, 1250, quanity, 1, 1, 1, 2500)
                counter = counter - 1
                print("Jeszcze tylko: ",counter)
                write2file_out(out, i, files, quanity) # generuje 16*3 plików XDDDDDD

                print("Wywolalem sie ")
    diff = time.time() - start_time
    diff = diff/60
    print("Trwałem: ",diff," minut")
    # x, y = np.where(best_bitmap[-1][1] == 1)
    # write2file_out(out,0,"kolka_i_kwadraty")
    # #write2file(x, y, i)
    # i = i + 1
    # print("Calosc wykonywala sie: ", time.time() - start_time2137)
    # x, y = np.where(best_bitmap[-1][1] == 1)
    # print(x)
    # print(y)
    # # write2file(x,y)
    # plt.plot(iterated, target_f, 'ro')
    # plt.show()
    # plt.plot(x, y, 'ro')
    # plt.axis([0, g.COLS - 1, 0, g.ROWS - 1])
    # x, y = np.where(best_bitmap[-1][0] == 1)
    # plt.plot(x, y, 'bx'
    #                '')
    # plt.axis([0, g.COLS - 1, 0, g.ROWS - 1])
    # plt.show()
    #
    # plt.show()
