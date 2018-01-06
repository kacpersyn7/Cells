from particle import *
from userequipment import *


class Target:
    def __init__(self, people=np.random.randint(0, 20, size=(g.COLS, g.ROWS)),
                 access_points_types=g.access_points_types, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.costs = np.array([x.cost for x in self.access_points])
        self.users_area = people

    def __call__(self, multidimensional_bitmap):
        result_area = np.zeros((self.x_size, self.y_size))
        for i in range(self.dimension):
            self.access_points[i].update_result_area(multidimensional_bitmap[i], result_area)
        total_aps = np.sum(multidimensional_bitmap, axis=(1, 2))
        total_cost = total_aps.dot(self.costs)
        new_area = self.users_area - result_area
        target = np.sum(new_area[np.where(new_area > 0)]) - total_cost
        return target
