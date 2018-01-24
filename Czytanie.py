import numpy as np
import matplotlib.pyplot as plt
import globals as g


def read_from_file_it_targ(name):
    it = []
    tf = []
    with open(name, 'r') as file:
        for line in file:
            parse = line.split()
            print(parse)
            it.append(int(parse[1]))
            tf.append(float(parse[3]))
    return it,tf


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

it,tf = read_from_file_it_targ("iterate_target_func_kolka_i_kwadraty_z_szumem_0_200")
it1,tf1 = read_from_file_it_targ("iterate_target_func_kolka_i_kwadraty_z_szumem_0_500")
it2,tf2 = read_from_file_it_targ("iterate_target_func_kolka_i_kwadraty_z_szumem_2_1000")
#
Heatmap = read_people_from_file("kolka_i_kwadraty_z_szumem",g.COLS,g.ROWS)
Wynik1 = read_people_from_file("outbitmapa_router_1_kolka_i_kwadraty_z_szumem_0_500 0",g.COLS,g.ROWS)
Wynik2 = read_people_from_file("outbitmapa_router_2_kolka_i_kwadraty_z_szumem_0_500 0",g.COLS,g.ROWS)
plt.imshow(Heatmap)
plt.show()
x, y = np.where(Wynik1 == 1)
x1, y1 = np.where(Wynik2 == 1)
plt.plot(x, y, 'bx')
plt.plot(x1, y1, 'ro')
plt.show()


plt.plot(it, tf, 'ro')
plt.plot(it1,tf1,'bx')
plt.plot(it2,tf2,'bo')
plt.show()