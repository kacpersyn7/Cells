import numpy as np


def generate_random(shape):
    users = np.random.rand(shape) * 100
    with open("rand_people", 'w') as file:
        x, y = np.where(users > 0)
        for i in range(len(x)):
            string = "x: " + str(x[i]) + " y: " + str(y[i]) + " power: " + str(int(users[x[i]][y[i]])) + "\n"
            file.write(string)

