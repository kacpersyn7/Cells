import time
import multiprocessing
from particle import *

def pso(func, lb=0, up=500, swarm_size=100, omega=1, phip=1, phig=1, maxiter=2000, start_time=time.time()):
    x_randoms = np.random.randint(lb, up, size=(swarm_size, func.dimension))
    particles = np.array([Particle(func, x_randoms[x]) for x in range(swarm_size)])
    g_iter = max(range(len(particles)), key=lambda i: particles[i].p_target)
    g_bitmap, g_target = particles[g_iter].get_local_best()
    for j in range(maxiter):
        for particle in particles:
            p_target = particle.iterate(g_bitmap, omega, phip, phig)
            if p_target > g_target:
                g_target = p_target
                g_bitmap = particle.get_p_bitmap()
        # pool = multiprocessing.Pool(4)
        # g_target, g_bitmap = pool.map(iterate_particles, [g_bitmap, omega, phip, phig, particles])
        if j%100 == 0:
            print("Czas wykonania to:",(time.time()-start_time))
            start_time=time.time()
            print("iteracja ", str(j), " wynik ", str(g_target))

    return g_bitmap, g_target
