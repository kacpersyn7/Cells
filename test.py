import math as mat
import random as ran

import matplotlib.pyplot as plt
import numpy as np
from numba import jit


def write2file(power, name):
    x, y = np.where(power > 0)
    string2 = name
    with open(string2, 'w') as file:
        for i in range(len(x)):
            string = "x: " + str(x[i]) + " y: " + str(y[i]) + " power: " + str(int(power[x[i]][y[i]])) + "\n"
            file.write(string)


@jit(nopython=True, parallel=True)
def generate_power_area(accespoint_area, max_range):
    new_area = np.zeros(accespoint_area.shape)  # alokuje statycznie pamiec
    for i in range(accespoint_area.shape[0]):  # iteruje ala C po calej macierzy
        for j in range(accespoint_area.shape[1]):
            if accespoint_area[i][j] == 1:  # jesli jest accespoint to oblicz dla niego moc
                for m in range(-max_range, max_range + 1):  # przejdz po otoczeniu
                    for n in range(-max_range, max_range + 1):
                        # print(m)
                        # print(n)                # Debugowy syf
                        # print("dupa")
                        if ((mat.sqrt(n * n + m * m)) <= max_range):  # zawez otoczenie do "kuli"
                            # print(float(max_range))
                            # print(mat.sqrt(n*n + m*m))             Debugowy syf
                            if ((i + n >= 0) & (i + n <= accespoint_area.shape[0] - 1) & (j + m >= 0) & (
                                    j + m <= accespoint_area.shape[1] - 1)):  # zachowanie na brzegach obszaru
                                if ((n != 0) | (m != 0)):  # zawezenie do siasiedztwa ( chyba)
                                    power = 250 / (mat.sqrt((n) * (n) + (m) * (m)))  # bieda wyliczenie mocy XD
                                    if power > new_area[i + n][j + m]:  # "wygrywa najsilniejszy"
                                        new_area[i + n][j + m] = power
    return new_area


def generate_area_square_linear(map, x_start, x_end, y_start, y_end, a, b, c):
    temp = map
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            tmp2 = c + a * (i - x_start) + b * (j - y_start)
            if temp[i][j] < tmp2:
                temp[i][j] = tmp2
    return temp


def make_noise(map, ilosc):
    temp = map
    for i in range(ilosc):
        x = ran.randint(0, 49)
        y = ran.randint(0, 49)
        if temp[x][y] == 0:
            temp[x][y] = ran.randint(100, 200)
    return temp


inna = np.zeros((50, 50))
nowa = np.zeros((50, 50))
nowa[20][20] = 1
nowa[40][40] = 1
nowa[10][40] = 1
nowa[0][1] = 1

inna = generate_power_area(nowa, 7)
inna[10][40] = 250
inna[0][1] = 250
inna[40][40] = 250
inna[20][20] = 250

kolejne = np.zeros((50, 50))
inna = generate_area_square_linear(inna, 20, 40, 10, 15, 7, 10, 100)
inna = generate_area_square_linear(inna, 30, 37, 15, 40, -5, -8, 250)

plt.imshow(inna)
plt.show()

write2file(inna, "kolka_i_kwadraty_z_szumwwwem")
