from accesspoint import *


##For more than one type of accesspoint

class Particle:
    def __init__(self, dimension, space, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.space = space
        # pointer to accesspoint types
        # great idea
        self.dimension = dimension
        self.result_area = np.zeros((x_size, y_size))
        self.x_bitmap = np.zeros((dimension, x_size, y_size))
        self.p_bitmap = np.zeros((dimension, x_size, y_size))
        self.velocity = np.zeros((dimension, x_size, y_size))
        self.x_target = 0.0

    def generate_first_individual(self, probability):
        for i in range(self.dimension):
            self.x_bitmap[i] = np.logical_not(
                np.logical_or(np.random.randint(0, probability[i], size=(self.x_size, self.y_size)), 0)).astype(int)

    def update_result_area(self):
        for i in range(self.dimension):
            self.space[i].update_result_area(self.x_bitmap[i], self.result_area)

    def target_function(self, users_area, costs):
        self.update_result_area()
        total_aps = np.sum(self.x_bitmap, axis=(1, 2))
        total_cost = total_aps.dot(costs)
        new_area = users_area - self.result_area
        self.x_target = np.sum(new_area[np.where(new_area > 0)]) - total_cost
        return self.x_target

    def calculate_velocity(self, global_best_bitmap, omega=1, fi_p=1, fi_g=1):
        self.velocity = omega * self.velocity + fi_p * (self.p_bitmap - self.x_bitmap) + fi_g * (
                global_best_bitmap - self.x_bitmap)

    def get_result_area(self):
        return self.result_area

    def get_ap_bitmap(self):
        return self.x_bitmap
