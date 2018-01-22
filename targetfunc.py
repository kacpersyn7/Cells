from particle import *
from userequipment import *


class Target:
    """Piszę po polsku, bo mało czasu. Klasa odpowiadająca za funkcję celu.
       Jako argumenty otrzymuje przestrzeń wymagań (ludzie),
       typy accesspointow(odpowiadajace za aktualizacje przestrzeni rozwiazan)
       oraz 2 funkcje: pierwsza będąca funkcją lub współczynnikiem dla wagi przestrzeni wymagań, druga wagi kosztów"""

    def __init__(self, people=np.random.randint(0, 20, size=(g.COLS, g.ROWS)),
                 access_points_types=g.access_points_types, people_function=lambda x: 10 * x,
                 cost_function=lambda x: 6*x):
        self.shape = people.shape
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.costs = np.array([x.cost for x in self.access_points])
        self.users_area = people
        self.people_function = people_function
        self.cost_function = cost_function

    def get_result_area(self, multidimensional_bitmap):
        result_area = np.zeros(self.shape)
        for i in range(self.dimension):
            result_area = self.access_points[i](multidimensional_bitmap[i], result_area)
        return result_area

    """Wywołanie funkcji celu dla wielowymiarowej bitmapy             czyli? accesspointow?? tylko obszaru zasiegów???          """
    def __call__(self, multidimensional_bitmap):
        total_aps = np.sum(multidimensional_bitmap, axis=(1, 2))
        total_cost = total_aps.dot(self.costs)
        new_area = self.get_result_area(multidimensional_bitmap) - self.users_area
        target = np.sum(new_area[np.where(self.users_area > 0)]) - total_cost
        return target
