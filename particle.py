from accesspoint import *


##For more than one type of accesspoint

class Particle:
    def __init__(self, target_func, lb, up):
        self.x_size = target_func.x_size
        self.y_size = target_func.y_size
        self.dimension = target_func.dimension
        self.target_func = target_func
        self.x_bitmap = np.random.randint(lb, up + 1, size=(self.dimension, self.x_size, self.y_size))
        self.velocity = np.random.randint(-abs(up - lb), abs(up - lb) + 1,
                                          size=(self.dimension, self.x_size, self.y_size))
        self.p_bitmap = np.copy(self.x_bitmap)
        self.x_target = self.target_func(self.x_bitmap)
        self.p_target = self.x_target

    def get_local_best(self):
        return self.p_bitmap, self.p_target

    def iterate(self, global_best, omega=0.5, phip=0.5, phig=0.5):
        self.calculate_velocity(global_best, omega, phip, phig)
        self.calculate_new_x()
        self.x_target = self.target_func(self.x_bitmap)
        if self.x_target > self.p_target:
            self.p_target = self.x_target
            self.p_target = np.copy(self.x_target)

    def calculate_velocity(self, global_best, omega=0.5, phip=0.5, phig=0.5):
        self.velocity = omega * self.velocity + phip * (self.p_bitmap - self.x_bitmap) + phig * (
                global_best - self.x_bitmap)
        # print(self.velocity)

    def calculate_new_x(self):
        for i in range(self.dimension):
            new = self.x_bitmap[i] + self.velocity[i]
            probability = (new - new.min()) / (new.max() - new.min())
            self.x_bitmap[i] = np.array([np.random.choice([0, 1], p=[1 - i, i]) for i in
                                         probability.reshape(self.x_size * self.y_size)]).reshape(
                (self.x_size, self.y_size))
