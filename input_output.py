import numpy as np


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
            if coords[0] < cols:
                if coords[1] < rows:
                    power = coords[-1]
                    people_heatmap[coords[0]][coords[1]] = power
    return people_heatmap


def write2file(num_array, name, index):
    x, y = np.where(num_array > 0)
    string2 = "out" + name + " " + str(index)
    with open(string2, 'w') as file:
        for i in range(len(x)):
            string = "x: " + str(x[i]) + " y: " + str(y[i]) + " power: " + str(int(num_array[x[i]][y[i]])) + "\n"
            file.write(string)


def write2file_out(out, index, people_f_name, population, omega, phip, phig):
    iterated, best_bitmap, target_f = zip(*out)
    string = "bitmapa_router_1_" + people_f_name + "_" + str(index) + "_" + str(population) + "_" + str(omega) + "_" + str(phip) + "_" + str(phig)
    write2file(best_bitmap[-1][0], string,index)
    string = "bitmapa_router_2_" + people_f_name + "_" + str(index) + "_" + str(population) + "_" + str(omega) + "_" + str(phip) + "_" + str(phig)
    write2file(best_bitmap[-1][1], string, index)
    string = "iterate_target_func_" + people_f_name + "_" + str(index) + "_" + str(population) + "_" + str(omega) + "_" + str(phip) + "_" + str(phig)
    with open(string, 'w') as file:
        for it in range(len(iterated)):
            string2 = "iterate " + str(iterated[it]) + " tarrget_func: " + str(target_f[it]) +  "\n"
            file.write(string2)


def read_from_file_it_targ(name):
    it = []
    tf = []
    with open(name, 'r') as file:
        for line in file:
            parse = line.split()
            print(parse)
            it.append(int(parse[1]))
            tf.append(float(parse[3]))
    return it, tf
