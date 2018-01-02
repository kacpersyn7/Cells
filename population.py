from particle import *
from userequipment import *


class Population:
    def __init__(self, population_size=100, access_points_types=g.access_points_types, x_size=g.COLS, y_size=g.ROWS):
        self.x_size = x_size
        self.y_size = y_size
        self.population_size = population_size
        self.dimension = len(access_points_types)
        self.access_points = [AccessPoint(**x) for x in access_points_types]
        self.costs = np.array([x.cost for x in self.access_points])
        self.individuals_list = np.array([Particle(self.dimension, self.access_points) for i in range(population_size)])
        self.global_best = 0
        self.global_best_bitmap = np.zeros((self.dimension, self.x_size, self.y_size))
        self.people = np.random.randint(0, 250, size=(self.x_size, self.y_size))

    def generate_first_population(self, low=1, high=100):
        random_list = np.random.uniform(low, high, size=(self.population_size, self.dimension))
        for i in range(self.population_size):
            self.individuals_list[i].generate_first_individual(random_list[i])
            self.update_individual(i)

    def calculate_target_function(self):
        for particle in self.individuals_list:
            particle.target_function(self.people, self.costs)  # arguments should be in particle class

    def get_individual(self, i):
        return self.individuals_list[i]
