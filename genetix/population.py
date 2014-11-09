import random

from chromosome import Chromosome


class Population(object):
    
    def __init__(self):
        self._chromosomes = list()
    
        self._generation = 0;
    
        self._selectionRate = 0.5
        self._crossoverRate = 0.7
        self._mutationRate = 0.0189
        
    def populate(self, count, genes):
        self._generation = 1;
        
        for i in range(0, count):
            chromosome = Chromosome()
            chromosome.addRandomGenes(genes)
            
            self._chromosomes.append(chromosome)
    
    def sort(self):
        # Set the fitness
        for i in range(0, len(self._chromosomes)):
            self._target.fitness(self._chromosomes[i])
            
        # Sort the list
        self._chromosomes.sort()
    
    def selection(self, target):
        self.setTarget(target)
        self.sort()
        
        # Get the count and how many to remove
        count = len(self._chromosomes)
        removeCount = int(count * self._selectionRate)
        
        # Remove the weak
        while removeCount < len(self._chromosomes):
            self._chromosomes.pop()
            
        # Create the new
        while count > len(self._chromosomes):
            # Pick two chromosomes
            x = random.randrange(0, len(self._chromosomes))
            y = random.randrange(0, len(self._chromosomes))
            
            # Add the new offspring
            chromosome = self.createOffspring(self._chromosomes[x], self._chromosomes[y])
            self._chromosomes.append(chromosome)
            
        # Increment generation  
        self._generation = self._generation + 1
        
    def generation(self):
        return self._generation
    
    def createOffspring(self, chromosomeX, chromosomeY):
        # Create new chromosom
        chromosome = Chromosome()
        
        # Get the number of genes & set the crossover
        geneCount = int((chromosomeX.length() + chromosomeY.length()) / 2)
        crossover = random.randrange(0, int(geneCount * self._crossoverRate))
        
        # Populate with X
        for i in range(0, crossover):
            chromosome.addGene(chromosomeX.gene(i))
            
        # Populate with Y
        for i in range(crossover, geneCount):
            chromosome.addGene(chromosomeY.gene(i))
            
        # Do the mutation
        mutation = int(10000 * self._mutationRate)
        for i in range(0, geneCount):
            if(random.randrange(0, 10000) < mutation):
                chromosome.mutateGene(i)
            
        # Return the new chromosome
        return chromosome
    
    def fittest(self):
        '''Returns the best fit out of the current population.
        '''
        self.sort()
        return self._chromosomes[(len(self._chromosomes) - 1)]
    
    def setTarget(self, target):
        self._target = target
    
    def setSelectionRate(self, selection):
        self._selectionRate = selection
        
    def setCrossoverRate(self, crossover):
        self._crossoverRate = crossover
        
    def setMutationRate(self, mutation):
        self._mutationRate = mutation