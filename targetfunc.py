from particle import *
import globals as g

@jit(nopython=True, parallel=True)
def sigmoid(x, L=200, k=10, x0=10):
    return L / (1 + np.exp(-k * (x - x0)))


class Target:
    """Piszę po polsku, bo mało czasu. Klasa odpowiadająca za funkcję celu.
       Jako argumenty otrzymuje przestrzeń wymagań (ludzie),
       typy accesspointow(odpowiadajace za aktualizacje przestrzeni rozwiazan),
       parametry - wspolczynnik wymagań, kosztów oraz parametry sigmoidy
       dzialajacej na roznice miedzy wymaganiami a sila sygnalu"""

    def __init__(self, people=np.random.randint(0, 20, size=(g.COLS, g.ROWS)),
                 access_points_types=g.access_points_types, cost_factor=1, people_factor=1, L=200, k=10, x0=10):
        self.shape = people.shape
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.costs = np.array([x.cost for x in self.access_points])
        self.users_area = people
        self.cost_factor = cost_factor
        self.people_factor = people_factor
        self.L = L
        self.k = k
        self.x0 = x0

    def get_result_area(self, multidimensional_bitmap):
        result_area = np.zeros(self.shape)
        for i in range(self.dimension):
            result_area = self.access_points[i](multidimensional_bitmap[i], result_area)
        return result_area

    """Wywołanie funkcji celu dla wielowymiarowej bitmapy accesspointow"""

    def __call__(self, multidimensional_bitmap):
        total_aps = np.sum(multidimensional_bitmap, axis=(1, 2))
        total_cost = total_aps.dot(self.costs)
        new_area = self.get_result_area(multidimensional_bitmap) - self.users_area
        target = self.people_factor * np.sum(
            self.users_area * sigmoid(new_area, self.L, self.k, self.x0)) - self.cost_factor * total_cost
        return target
