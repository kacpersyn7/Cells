from particle import *


def pso(func, lb=0, up=380, swarm_size=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100):
    x_randoms = np.random.randint(lb, up, size=(swarm_size, func.dimension))
    velocity_randoms = np.random.randint(lb, up, size=(swarm_size, func.dimension))
    particles = np.array([Particle(func, x_randoms[x], velocity_randoms[x]) for x in range(swarm_size)])
    # We have particles
    g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
    g_array, g_target = particles[g_iter].get_local_best()
    for j in range(maxiter):
        for particle in particles:
            particle.iterate(g_array, omega, phip, phig)
            g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
            g_array, g_target = particles[g_iter].get_local_best()
    return g_array, g_target
