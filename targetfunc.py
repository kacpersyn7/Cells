from particle import *
from userequipment import *


class Target:
    def __init__(self, people=np.random.randint(0, 20, size=(g.COLS, g.ROWS)),
                 access_points_types=g.access_points_types):
        self.x_size = people.shape[0]
        self.y_size = people.shape[1]
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.costs = np.array([x.cost for x in self.access_points])
        self.users_area = people
        self.result_area = np.zeros((self.x_size, self.y_size))

    def __call__(self, multidimensional_bitmap):
        for i in range(self.dimension):
            self.result_area = self.access_points[i].update_result_area(multidimensional_bitmap[i], self.result_area)
        total_aps = np.sum(multidimensional_bitmap, axis=(1, 2))
        total_cost = total_aps.dot(self.costs)
        new_area = self.result_area - self.users_area
        target = 10 * np.sum(new_area[np.where(self.users_area > 0)]) - total_cost
        self.result_area = np.zeros((self.x_size, self.y_size))
        return target
