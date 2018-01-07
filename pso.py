from particle import *


def pso(func, lb=0, up=380, swarm_size=100, omega=1, phip=1, phig=1, maxiter=100):
    x_randoms = np.random.randint(lb, up, size=(swarm_size, func.dimension))
    velocity_randoms = np.random.randint(lb, up, size=(swarm_size, func.dimension))
    particles = np.array([Particle(func, x_randoms[x], velocity_randoms[x]) for x in range(swarm_size)])
    # We have particles
    g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
    g_array, g_target = particles[g_iter].get_local_best()
    iter = 0
    j = 0
    for j in range(maxiter):
        for particle in particles:
            a, b = particle.iterate(g_array, g_target, omega, phip, phig)
            if a is not None:
                g_array, g_target = a, b
        print("iteracja " + str(j))
        j += 1

    return g_array, g_target
