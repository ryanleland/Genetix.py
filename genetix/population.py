import random
import operator

from chromosome import Chromosome


class Population(object):

    def __init__(self, fitness_function=None, selection_rate=0.5, crossover_rate=0.5, mutation_rate=0.0002):
        self.fitness_function = fitness_function
        self.selection_rate = selection_rate
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

        self.population = []
        self.population_size = 0
        self.gene_count = 0

        self.best_fit = None
        self.best_fit_fitness = 0

    def populate(self, population_size, chromosome_blueprint):
        self.population_size = population_size
        self.gene_count = len(chromosome_blueprint)

        for n in range(0, population_size):
            c = Chromosome()
            c.construct(chromosome_blueprint)

            self.population.append(c)

    def evolve(self, generations):
        if not self.fitness_function:
            raise Exception("Please supply a fitness function to evolve population.")

        if not len(self.population):
            raise Exception("Can't evolve an empty population. Please run populate method.")

        for generation in range(0, generations):
            random.seed()
            self.multiply(self.select())

            yield generation + 1

    def fittest(self):
        return self.best_fit, self.best_fit_fitness

    def select(self):
        selected = []
        selection_count = int(self.population_size * self.selection_rate)

        # Evaluate each chromosome
        for chromosome in self.population:
            fitness = self.evaluate(chromosome)
            selected.append((chromosome, fitness))

        # Get the selection.
        selected = sorted(selected, key=operator.itemgetter(1), reverse=True)[:selection_count]
        
        selection = selected[0]
        if selection[1] > self.best_fit_fitness:
            self.best_fit_fitness = selection[1]
            self.best_fit = selection[0]

        # Create the new population.
        self.population = [s[0] for s in selected]

        return [s[0] for s in selected]

    def multiply(self, selected):
        '''Generate offspring until we're back to the right population size.
        '''
        while len(self.population) < self.population_size:
            x = random.choice(selected)
            y = random.choice(selected)

            chromosome = Chromosome()
            chromosome.offspring(x, y, self.crossover_rate, self.mutation_rate)
            
            self.population.append(chromosome)

    def evaluate(self, chromosome):
        return self.fitness_function(chromosome)

    def fitness(self, fitness_function):
        self.fitness_function = fitness_function
