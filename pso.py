from particle import *


def pso(func, lb=0, up=390, swarm_size=200, omega=1, phip=1, phig=1, maxiter=500):
    x_randoms = np.random.randint(lb, up, size=(swarm_size, func.dimension))
    particles = np.array([Particle(func, x_randoms[x]) for x in range(swarm_size)])
    # We have particles
    g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
    g_array, g_target = particles[g_iter].get_local_best()
    for j in range(maxiter):
        for particle in particles:
            a, b = particle.iterate(g_array, g_target, omega, phip, phig)
            if a is not None:
                g_array, g_target = a, b
        print("iteracja " + str(j) + " wynik " + str(g_target))

    return g_array, g_target
