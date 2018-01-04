from accesspoint import *


##For more than one type of accesspoint

class Particle:
    def __init__(self, dimension, space, costs, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.space = space
        self.costs = costs
        # pointer to accesspoint types
        # great idea
        self.dimension = dimension
        self.result_area = np.zeros((x_size, y_size))
        self.x_bitmap = np.zeros((dimension, x_size, y_size))
        self.p_bitmap = np.zeros((dimension, x_size, y_size))
        self.velocity = np.zeros((dimension, x_size, y_size))
        self.x_target = 0.0
        self.p_target = 0.0

    def generate_first_individual(self, number_of_aps):
        for i in range(self.dimension):
            temp_array = np.zeros(self.x_size * self.y_size)
            print(number_of_aps[i])
            temp_array[:number_of_aps[i]] = 1
            np.random.shuffle(temp_array)
            self.x_bitmap[i] = temp_array.reshape(self.x_size, self.y_size)

    def update_result_area(self):
        for i in range(self.dimension):
            self.space[i].update_result_area(self.x_bitmap[i], self.result_area)

    def target_function(self, users_area):
        self.update_result_area()
        total_aps = np.sum(self.x_bitmap, axis=(1, 2))
        total_cost = total_aps.dot(self.costs)
        new_area = users_area - self.result_area
        self.x_target = np.sum(new_area[np.where(new_area > 0)]) - total_cost
        if self.x_target > self.p_target:
            self.p_bitmap = np.copy(self.x_bitmap)
            self.p_target = self.x_target
        return self.p_target

    def calculate_velocity(self, global_best_bitmap, omega=1, fi_p=1, fi_g=1):
        self.velocity = omega * self.velocity + fi_p * (self.p_bitmap - self.x_bitmap) + fi_g * (
                global_best_bitmap - self.x_bitmap)

    def calculate_new_x(self):
        probability_bitmap = self.x_bitmap + self.velocity
        return probability_bitmap

    def get_result_area(self):
        return self.result_area

    def get_ap_bitmap(self):
        return self.x_bitmap
