from individual import *
from userequipment import *


class Individuals:
    def __init__(self, population_size=100, access_points_types=g.access_points_types, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.population_size = population_size
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.individuals_list = [Individual(self.dimension) for i in range(population_size)]

    def generate_first_population(self, low=1, high=100):
        random_list = np.random.uniform(low, high, size=(self.population_size, self.dimension))
        for i in range(self.population_size):
            self.individuals_list[i].generate_first_individual(random_list[i])
            self.update_individual(i)

    def update_individual(self, i):
        for j in range(self.dimension):
            self.individuals_list[i].update_result_area(self.access_points[j].access_area_fun,
                                                        self.access_points[j].get_power, j)
