import numba
import numpy as np


@numba.jit(nopython=True, cache=True)
def update_result_area_outer(ap_bitmap, radius, result_area, x_size, y_size, circle):
    access_points = np.where(ap_bitmap == 1)
    for x, y in zip(access_points[0], access_points[1]):
        diff_x = radius - x
        diff_y = radius - y
        diff_x_2 = -diff_x
        diff_y_2 = -diff_y
        if diff_x < 0:
            diff_x = 0
        else:
            diff_x_2 = 0
        if diff_y < 0:
            diff_y = 0
        else:
            diff_y_2 = 0

        result_area[diff_x_2:(x + radius + 1), diff_y_2:(y + radius + 1)] = np.maximum(
            result_area[diff_x_2:(x + radius + 1), diff_y_2:(y + radius + 1)],
            (circle[diff_x:(radius + x_size - x), diff_y:(radius + y_size - y)]))
    return result_area


class AccessPoint:
    """Klasa odpowiadająca za tworzenie różnych typów accesspointów. Jako argumenty przyjmuje:
    koszt, maksymalną moc, zasięg, funkcję mocy w zależności od odległości euklidesowej.
    Jest funktorem - wywołanie aktualizuje przestrzen rozwiazan."""

    def __init__(self, cost=100, max_power=10, radius=16, access_area_fun=lambda point: point[0] ** 2 + point[1] ** 2):
        self.max_power = max_power
        self.access_area_fun = access_area_fun
        self.cost = cost
        self.radius = radius
        self.circle = self.init_circle()

    def get_power(self, dist):
        return (1. / (dist * 0.7)) * self.max_power

    def init_circle(self):
        circle = np.copy(
            self.access_area_fun(np.ogrid[-self.radius:(self.radius + 1), -self.radius:(self.radius + 1)])).astype(
            float)
        circle[circle > self.radius ** 2] = -1
        circle.itemset((self.radius, self.radius), 0.5)
        circle = self.get_power(circle)
        circle[circle < 0] = 0
        return circle

    """Aktualizacja przestrzeni rozwiązań dla tych parametrów."""

    def __call__(self, ap_bitmap, result_area):
        result_area = update_result_area_outer(ap_bitmap, self.radius, result_area, result_area.shape[0],
                                               result_area.shape[1],
                                               self.circle)
        return result_area
