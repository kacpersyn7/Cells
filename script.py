import matplotlib.pyplot as plt

from pso import *
from targetfunc import *

def read_people_from_file(name, rows, cols):
    """ Czyta bitmape ludzi z pliku, jako argument przyjmuje nazwe pliku i zwraca zczytaną bitmapę"""
    people_heatmap = np.zeros((rows, cols))
    with open(name,'r') as file:
        for line in file:
            parse = line.split()
            coords = []
            for char in parse:
                if char.isnumeric():
                    coords.append(int(char))
            print(coords)
            if coords[0] < cols:
                if coords[1] < rows:
                    power = coords[-1]
                    people_heatmap[coords[0]][coords[1]] = power
    return people_heatmap

def write2file(x,y, index):
    string2 = "out" + str(index)
    with open(string2,'w') as file:
        for i in range(len(x)):
            string = "x: " + str(x[i]) + " y: " + str(y[i]) + "\n"
            file.write(string);


if __name__ == "__main__":
    people = read_people_from_file("rand_people",g.ROWS,g.COLS)
    my_func = Target(people)
    population = 500 #
    omega = [0.9, 1, 1.1] #
    phig = [0.9, 1, 1.1] #
    phip = [0.9, 1, 1.1] #
    min_rand = [0, 400, 1000]
    max_rand = [1100, 1900, 2500]
    max_iter = 1000
    i = 0
    start_time2137= time.time()
    for om in omega:
        for g in phig:
            for p in phip:
                for m_r in min_rand:
                    for ma_r in max_rand:
                        best_bitmap, best_value = pso(my_func, m_r, ma_r, population, om, p, g, max_iter)
                        x, y = np.where(best_bitmap[1] == 1)
                        write2file(x, y, i)
                        i = i + 1
    print("Calosc wykonywala sie: ", time.time()-start_time2137)
    x, y = np.where(best_bitmap[1] == 1)
    print(x)
    print(y)
    write2file(x,y)
    plt.plot(x, y, 'ro')
    plt.axis([0, g.COLS-1, 0, g.ROWS-1])
    x, y = np.where(best_bitmap[0] == 1)
    plt.plot(x, y, 'bx'
                   '')
    plt.axis([0, g.COLS-1, 0, g.ROWS-1])
    plt.show()


    plt.show()
