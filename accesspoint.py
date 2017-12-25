from area import *


class AccessPoint(Area):

    def __init__(self, area, max_power=10, max_range=10, access_area_fun=lambda x, y: x * x + y * y <= 16,
                 dist_fun=lambda diff_x, diff_y: (diff_x * diff_x + diff_y * diff_y).astype(float)):
        self.area = area
        self.max_power = max_power
        self.max_range = max_range
        self.activate_area = access_area_fun
        self.dist_fun = dist_fun

    def generate_individual(self):
        self.area.area = self.generate_random(1)

    # def generate_ap_individuals(self, n_of_individuals):
    #     individuals = np.zeros((n_of_individuals, self.area.x_size, self.area.y_size))
    #     for i in range(n_of_individuals):
    #         individuals[i] = self.generate_random(i)
    #     return individuals

    def get_power(self, ue_x, ue_y):
        return self.max_power * self.power_fun(ue_x, ue_y)

    def set_bit(self, x, y):
        self.area[x][y] = 1

    def reset_bit(self, x, y):
        self.area[x][y] = 0

    def get_power(self, ap_x, ap_y, ue_x, ue_y):
        distance = self.dist_fun(ue_x - ap_x, ue_y - ap_y)
        distance[np.where(distance == 0)[0]] = 0.5
        print(distance)
        return (1. / distance) * self.max_power

    def update_result_area(self, result_area):
        accesspoints = np.where(self.area.area == 0)
        new_result_area = np.copy(result_area)
        for x, y in zip(accesspoints[0], accesspoints[1]):
            temp_y, temp_x = np.ogrid[-x:self.area.size_x - x, -y:self.area.size_y - y]
            mask_indexes = np.where(self.activate_area(temp_x, temp_y))
            print(mask_indexes)
            new_result_area[mask_indexes] = self.get_power(x, y, mask_indexes[0], mask_indexes[1])
            diff = np.where((new_result_area - result_area) < 0)
            new_result_area[diff] = result_area[diff]
            result_area = np.copy(new_result_area)

    def get_bitmap(self):
        return np.logical_not(np.logical_or(self.area.area, 0)).astype(int)
