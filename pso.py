import numpy as np


def init_individual(particle_bitmap, number_of_aps):
    for i in range(particle_bitmap.shape[0]):
        temp_array = np.zeros(particle_bitmap.shape[1] * particle_bitmap.shape[2])
        print(number_of_aps[i])
        temp_array[:number_of_aps[i]] = 1
        np.random.shuffle(temp_array)
        particle_bitmap[i] = temp_array.reshape(particle_bitmap.shape[1], particle_bitmap.shape[2])


def init_swarm(bitmap_vect, low=1, high=100):
    random_list = np.random.randint(low, high, size=(bitmap_vect.shape[0], bitmap_vect.shape[1]))
    for i in range(bitmap_vect.shape[0]):
        init_individual(bitmap_vect[i], random_list[i])


def calculate_velocity(self, global_best_bitmap, omega=1, fi_p=1, fi_g=1):
    self.velocity = omega * self.velocity + fi_p * (self.p_bitmap - self.x_bitmap) + fi_g * (
            global_best_bitmap - self.x_bitmap)


def calculate_new_x(self):
    probability_bitmap = self.x_bitmap + self.velocity
    return probability_bitmap


def pso(func, dimension, x_size, y_size, lb, ub, swarm_size=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100):
    x_bitmap = np.zeros((swarm_size, dimension, x_size, y_size))
    init_swarm(x_bitmap, lb, ub)
    p_bitmap = np.copy(x_bitmap)
    # velocity = np.zeros((swarm_size, dimension, x_size, y_size))
    x_target = np.array([func(x) for x in x_bitmap])
    g_iter = np.argmax(x_target)
    g_bitmap = np.copy(x_bitmap[g_iter])
    p_target = np.copy(x_target)
    g_target = x_target[g_iter]
    ##Mabye dict/class particle with xi, vi, pi
    return x_target, x_bitmap
