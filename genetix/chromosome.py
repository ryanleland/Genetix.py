import random


class Chromosome(object):
    def __init__(self):
        self._genes = list()

    def __cmp__(self, other):
        return cmp(self.fitness(), other.fitness())

    def fitness(self):
        return self._fitness
        
    def set_fitness(self, fitness):
        self._fitness = fitness
        
    def add_gene(self, gene):
        self._genes.append(bool(gene))
        
    def add_random_genes(self, count):
        # Seed the random number generator
        random.seed()
    
        for i in range(0, count):
            self.add_gene(random.randrange(0, 2))
        
    def genes(self):
        return self._genes
    
    def gene(self, i):
        return self._genes[i]
        
    def mutate_gene(self, i):
        self._genes[i] = bool(random.randrange(0, 2))
        
    def length(self):
        return len(self._genes)