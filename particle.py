from accesspoint import *


##For more than one type of accesspoint

class Particle:
    def __init__(self, target_func, x_randoms, velocity_randoms):
        self.x_size = target_func.x_size
        self.y_size = target_func.y_size
        self.dimension = target_func.dimension
        self.target_func = target_func
        # self.x_bitmap = np.random.randint(lb, up + 1, size=(self.dimension, self.x_size, self.y_size))
        # self.velocity = np.random.randint(-abs(up - lb), abs(up - lb) + 1,
        #                                   size=(self.dimension, self.x_size, self.y_size))
        self.x_bitmap = self.init_particle(x_randoms)
        self.velocity = np.zeros((self.dimension, self.x_size, self.y_size))
        self.p_bitmap = np.copy(self.x_bitmap)
        self.x_target = self.target_func(self.x_bitmap)
        self.p_target = self.x_target

    def init_particle(self, number_of_aps):
        temp_multi_array = np.zeros((self.dimension, self.x_size, self.y_size))
        for i in range(self.dimension):
            temp_array = np.zeros(self.x_size * self.y_size)
            print(number_of_aps[i])
            temp_array[:number_of_aps[i]] = 1
            np.random.shuffle(temp_array)
            temp_multi_array[i] = temp_array.reshape(self.x_size, self.y_size)
        return temp_multi_array

    def get_local_best(self):
        return self.p_bitmap, self.p_target

    def iterate(self, global_best, omega=1, phip=1, phig=1):
        self.velocity = omega * self.velocity + phip * (self.p_bitmap - self.x_bitmap) + phig * (
                global_best - self.x_bitmap)
        print(self.velocity)
        self.calculate_new_x()
        self.x_target = self.target_func(self.x_bitmap)
        if self.x_target > self.p_target:
            self.p_target = self.x_target
            self.p_target = np.copy(self.x_target)

    def calculate_new_x(self):
        for i in range(self.dimension):
            new = self.x_bitmap[i] + self.velocity[i]
            probability = (new - new.min()) / (new.max() - new.min())
            self.x_bitmap[i] = np.array([np.random.choice([0, 1], p=[1 - i, i]) for i in
                                         probability.reshape(self.x_size * self.y_size)]).reshape(
                (self.x_size, self.y_size))
