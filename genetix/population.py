import random

from chromosome import Chromosome


class Population(object):
    
    def __init__(self, selection_rate=0.5, crossover_rate=0.7, mutation_rate=0.0189):
        self._chromosomes = list()
    
        self._generation = 0;
    
        self._selection_rate = selection_rate
        self._crossover_rate = crossover_rate
        self._mutation_rate = mutation_rate
        
    def populate(self, count, genes):
        self._generation = 1;
        
        for i in range(0, count):
            chromosome = Chromosome()
            chromosome.add_random_genes(genes)
            
            self._chromosomes.append(chromosome)
    
    def sort(self):
        # Set the fitness
        for i in range(0, len(self._chromosomes)):
            self._target.fitness(self._chromosomes[i])
            
        # Sort the list
        self._chromosomes.sort()
    
    def selection(self, target):
        self.set_target(target)
        self.sort()
        
        # Get the count and how many to remove
        count = len(self._chromosomes)
        removeCount = int(count * self._selection_rate)
        
        # Remove the weak
        while removeCount < len(self._chromosomes):
            self._chromosomes.pop()
            
        # Create the new
        while count > len(self._chromosomes):
            # Pick two chromosomes
            x = random.randrange(0, len(self._chromosomes))
            y = random.randrange(0, len(self._chromosomes))
            
            # Add the new offspring
            chromosome = self.create_offspring(self._chromosomes[x], self._chromosomes[y])
            self._chromosomes.append(chromosome)
            
        # Increment generation  
        self._generation += 1
        
    def generation(self):
        return self._generation
    
    def create_offspring(self, chromosomeX, chromosomeY):
        # Create new chromosom
        chromosome = Chromosome()
        
        # Get the number of genes & set the crossover
        geneCount = int((chromosomeX.length() + chromosomeY.length()) / 2)
        crossover = random.randrange(0, int(geneCount * self._crossover_rate))
        
        # Populate with X
        for i in range(0, crossover):
            chromosome.add_gene(chromosomeX.gene(i))
            
        # Populate with Y
        for i in range(crossover, geneCount):
            chromosome.add_gene(chromosomeY.gene(i))
            
        # Do the mutation
        mutation = int(10000 * self._mutation_rate)
        for i in range(0, geneCount):
            if(random.randrange(0, 10000) < mutation):
                chromosome.mutate_gene(i)
            
        # Return the new chromosome
        return chromosome
    
    def fittest(self):
        '''Returns the best fit out of the current population.
        '''
        self.sort()
        return self._chromosomes[(len(self._chromosomes) - 1)]
    
    def set_target(self, target):
        self._target = target
