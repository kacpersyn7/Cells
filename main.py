import numpy as np
import random as rand
import math as mat

def generate_area(x, y, resolution):
    area = np.zeros((x,y))
    return area

def generate_solution(current_area):
    amount = rand.randint(0, current_area.size)
    new_area = np.zeros(current_area.shape)
    for i in range(amount):
        not_equal=1
        while(not_equal):
            x_coord = rand.randint(0,current_area.shape[0]-1) # losuje koordynaty
            y_coord = rand.randint(0,current_area.shape[1]-1)
            if new_area[x_coord][y_coord] == 0:
                not_equal = 0
                new_area[x_coord][y_coord] = 1
    return new_area

def generate_power_area(accespoint_area, max_range): # generuje obszar mocy XD, tj macierz z wartosciami mocy w kazdym punkcie
    new_area = np.zeros(accespoint_area.shape) # alokuje statycznie pamiec
    for i in range(accespoint_area.shape[0] - 1): # iteruje ala C po calej macierzy
        for j in range(accespoint_area.shape[1] - 1):

            if accespoint_area[i][j] == 1: # jesli jest accespoint to oblicz dla niego
                for m in range(-max_range, max_range+1): # przejdz po otoczeniu
                    for n in range(-max_range, max_range+1):
                        #print(m)
                        #print(n)                 Debugowy syf
                        #print()
                        if((mat.sqrt(n*n + m*m)) <= max_range): # zawez otoczenie do "kuli"
                            #print(float(max_range))
                            #print(mat.sqrt(n*n + m*m))             Debugowy syf
                            if((i + n >= 0) & (i + n <= accespoint_area.shape[0]-1) & (j + m >= 0) & (j + m <= accespoint_area.shape[1]-1)): # zachowanie na brzegach obszaru
                                if((n != 0) | (m!=0) ): # zawezenie do siasiedztwa ( chyba)
                                    power = 10/(mat.sqrt((n)*(n) + (m)*(m))) # bieda wyliczenie mocy XD
                                    if power > new_area[i+n][j+m]: # "wygrywa najsilniejszy"
                                        new_area[i+n][j+m] = power
    return new_area # zwraca obszar mocy

def number_of_accesspoints(accesspoinnt_area): # wylicza liczbe kupionych ruterow
    number = 0
    for i in range(accesspoinnt_area.shape[0] - 1):
        for j in range(accesspoinnt_area.shape[1] - 1):
            number = number + 1
    return number




def generate_users_area(current_area): # generuje uzytkownikow, potrzebowalem do testow
    amount = rand.randint(0, current_area.size)
    new_area = np.zeros(current_area.shape)
    for i in range(amount):
        not_equal=1
        while(not_equal):
            x_coord = rand.randint(0,current_area.shape[0]-1)
            y_coord = rand.randint(0,current_area.shape[1]-1)
            if new_area[x_coord][y_coord] == 0:
                not_equal = 0
                new_area[x_coord][y_coord] = rand.randint(0,5) # losuj do 5 uzytkownikow
    return new_area

def target_function(power_area, accesspoint_area, users_area, cost_of_accesspoint):
    value = 0;
    number = number_of_accesspoints(accesspoint_area)
    for i in range(power_area.shape[0] - 1):
        for j in range(power_area.shape[1] - 1):
            value = value + power_area[i][j]*users_area[i][j]
        value = value - cost_of_accesspoint*number # odejmuje koszt accesspointow
    return value



w = generate_area(4 ,4 ,12)
d = generate_solution(w)
power_map = generate_power_area(d, 2)
user_map = generate_users_area(w)
a = w.size
wynik = target_function(power_map,d, user_map, 100)
print(wynik)
print(user_map)
print(2)
print(1)
print(power_map)
print(wynik)