from individual import *
from userequipment import *


class Individuals:
    def __init__(self, population_size=100, access_points_types=g.access_points_types, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.population_size = population_size
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.costs = np.array([x.cost for x in self.access_points])
        self.individuals_list = np.array([Individual(self.dimension) for i in range(population_size)])
        self.global_best = 0
        self.global_best_id = 0

    def generate_first_population(self, low=1, high=100):
        random_list = np.random.uniform(low, high, size=(self.population_size, self.dimension))
        for i in range(self.population_size):
            self.individuals_list[i].generate_first_individual(random_list[i])
            self.update_individual(i)

    def update_individual(self, i):
        for ap_id in range(self.dimension):
            self.individuals_list[i].update_result_area(self.access_points[ap_id].access_area_fun,
                                                        self.access_points[ap_id].get_power, ap_id)

    def update_every_individual(self):
        for i in range(self.population_size):
            self.update_individual(i)

    def calculate_target_function(self):
        self.update_every_individual()
        self.global_best = max(individual.target_function(self.costs) for individual in self.individuals_list)
        self.global_best_id = np.where(self.individuals_list == self.global_best)
