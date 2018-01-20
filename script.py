import matplotlib.pyplot as plt

from pso import *
from targetfunc import *

def read_people_from_file(name, rows, cols):
    """ Czyta bitmape ludzi z pliku, jako argument przyjmuje nazwe pliku i zwraca zczytana bitmapę"""
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

def write2file(x,y):
    with open("out.log",'w') as file:
        for i in range(len(x)):
            string = "x: " + str(x[i]) + " y: " + str(y[i]) + "\n"
            file.write(string);


if __name__ == "__main__":
    people = read_people_from_file("template_people",g.ROWS,g.COLS)
    my_func = Target(people)
    best_bitmap, best_value = pso(my_func, 0, 300, 200, 1, 1, 1, 1000)

    x, y = np.where(best_bitmap[1] == 1)
    print(x)
    print(y)
    write2file(x,y)
    plt.plot(x, y, 'ro')
    plt.axis([0, g.COLS-1, 0, g.ROWS-1])
    plt.show()
