import numpy as np
import random as rand

def generate_area(x, y, resolution):
    area = np.zeros((x,y))
    return area

def generate_solution(current_area):
    amount = rand.randint(0, current_area.size)
    new_area = np.zeros(current_area.shape)
    for i in range(amount):
        not_equal=1
        while(not_equal):
            x_coord = rand.randint(0,current_area.shape[0]-1)
            y_coord = rand.randint(0,current_area.shape[1]-1)
            if new_area[x_coord][y_coord] == 0:
                not_equal = 0
                new_area[x_coord][y_coord] = 1
    return new_area


w = generate_area(100 ,100 ,12)
d = generate_solution(w)
a = w.size
print(d.size)