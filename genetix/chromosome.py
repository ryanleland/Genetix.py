import random


class Chromosome(object):
    def __init__(self):
        self._genes = list()

    def __cmp__(self, other):
        return cmp(self.fitness(), other.fitness())

    def fitness(self):
        return self._fitness
        
    def setFitness(self, fitness):
        self._fitness = fitness
        
    def addGene(self, gene):
        self._genes.append(bool(gene))
        
    def addRandomGenes(self, count):
        # Seed the random number generator
        random.seed()
    
        for i in range(0, count):
            self.addGene(random.randrange(0, 2))
        
    def genes(self):
        return self._genes
    
    def gene(self, i):
        return self._genes[i]
        
    def mutateGene(self, i):
        self._genes[i] = bool(random.randrange(0, 2))
        
    def length(self):
        return len(self._genes)