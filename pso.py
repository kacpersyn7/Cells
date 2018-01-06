from particle import *


def generate_first_individual(self, number_of_aps):
    for i in range(self.dimension):
        temp_array = np.zeros(self.x_size * self.y_size)
        print(number_of_aps[i])
        temp_array[:number_of_aps[i]] = 1
        np.random.shuffle(temp_array)


def pso(func, lb=0, up=400, swarm_size=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100):
    x_randoms = np.random.randint(lb, up, size=(2, swarm_size))
    velocity_randoms = np.random.randint()
    particles = np.array([Particle(func, lb, up) for x in range(swarm_size)])
    # We have particles
    g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
    g_array, g_target = particles[g_iter].get_local_best()
    for j in range(maxiter):
        for particle in particles:
            particle.iterate(g_array, omega, phip, phig)
            g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
            g_array, g_target = particles[g_iter].get_local_best()
    return g_array, g_target
