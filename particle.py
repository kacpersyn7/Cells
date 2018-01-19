from numba import jit

from accesspoint import *


@jit(nopython=True, parallel=True)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class Particle:
    def __init__(self, target_func, x_randoms):
        self.x_size = target_func.shape[0]
        self.y_size = target_func.shape[1]
        self.dimension = target_func.dimension
        self.target_func = target_func
        self.x_bitmap = self.init_particle(x_randoms)
        self.velocity = np.zeros((self.dimension, self.x_size, self.y_size))
        self.p_bitmap = np.copy(self.x_bitmap)
        self.x_target = self.target_func(self.x_bitmap)
        self.p_target = self.x_target

    def init_particle(self, number_of_aps):
        temp_multi_array = np.zeros((self.dimension, self.x_size, self.y_size))
        for i in range(self.dimension):
            temp_array = np.zeros(self.x_size * self.y_size)
            temp_array[:number_of_aps[i]] = 1
            np.random.shuffle(temp_array)
            temp_multi_array[i] = temp_array.reshape(self.x_size, self.y_size)
        return temp_multi_array

    def get_local_best(self):
        return self.p_bitmap, self.p_target

    def get_p_bitmap(self):
        return self.p_bitmap

    def iterate(self, global_best, omega=1, phip=1, phig=1):
        self.velocity = omega * self.velocity + phip * (self.p_bitmap - self.x_bitmap) + phig * (
                global_best - self.x_bitmap)
        self.calculate_new_x()
        self.x_target = self.target_func(self.x_bitmap)
        if self.x_target > self.p_target:
            self.p_target = self.x_target
            self.p_bitmap = np.copy(self.x_bitmap)
        return self.p_target

    def calculate_new_x(self):
        probability = sigmoid(self.velocity)
        self.x_bitmap = np.logical_not(
            np.random.random_sample((self.dimension, self.x_size, self.y_size)) >= probability).astype(int)
