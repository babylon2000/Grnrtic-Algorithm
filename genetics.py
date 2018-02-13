import numpy as np
import random as rnd

class GeneticAlgorithm:

    def __init__(self, population, size_of_population, fitness):
        self.size_of_population = size_of_population
        self.fitness = fitness
        self.population = population
        for i in range(self.size_of_population):
            self.population[i] = rnd.randrange(-6, 6)
            self.fitness[i] = self.fitness_func(population[i])
            pass
        pass

    def fitness_func(self, x):
        return -x * x + 2

    def max_index(self, ar):
        max = ar[0]
        max_ind = 0
        for i in range(1, len(ar)):
            if (max < ar[i]):
                max_ind = i
                pass
            pass
        return max_ind

    def reproduction(self, parent, child, size_p, b):
        for i in range(0, size_p, 2):
            child[i] = b * parent[i] + (1 - b) * parent[i + 1]
            child[i + 1] = b * parent[i + 1] + (1 - b) * parent[i]
            pass
        pass

    def after_reproduction(self, parent, child):
        return np.concatenate((parent, child))

    def selection(self, population, buff, fit):
        total_fitness = self.after_reproduction((buff, fit))


    pass


size_of_pop = 10
pop = np.zeros((size_of_pop, 1))
offspring = np.zeros((size_of_pop, 1))
fit = np.zeros((size_of_pop, 1))
num_of_iter = 0
buffer = np.zeros((size_of_pop, 1))
n = GeneticAlgorithm(pop, size_of_pop, fit)
print('\n', n.fitness)

for epoch in range(10):
    n.reproduction(pop, offspring, size_of_pop, 0.2)
    pop = n.after_reproduction(pop, offspring)
    for i in range(size_of_pop, 2*size_of_pop):
        buffer[i - size_of_pop] = n.fitness[i - size_of_pop]
        n.fitness[i - size_of_pop] = n.fitness_func(pop[i])
        pass
    num_of_iter += 1
    pass

print(n.fitness)
print('\n', buffer)
