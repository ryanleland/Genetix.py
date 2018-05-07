# -*- coding: utf-8 -*-

import random
import operator

from genetix.chromosome import Chromosome


class Population(object):

    def __init__(self, fitness_function=None, selection_rate=0.7, crossover_rate=1.0, mutation_rate=0.05):
        self.fitness_function = fitness_function
        self.selection_rate = selection_rate
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

        self.chromosomes = []
        self.size = 0
        self.gene_count = 0

        self.best_fit = None
        self.best_fit_fitness = 0

    def populate(self, size, chromosome_blueprint):
        self.size = size
        self.gene_count = len(chromosome_blueprint)

        for n in range(0, size):
            c = Chromosome.construct(chromosome_blueprint)
            self.chromosomes.append(c)

    def evolve(self, generations):
        """A generator for evolving the population. Will yield each generation
        to provide a hook for logging best fit over time, or any other
        monitoring that might be required.
        """
        if not self.fitness_function:
            raise PopulationException("Please supply a fitness function to evolve population.")

        if not len(self.chromosomes):
            raise PopulationException("Can't evolve an empty population. Please run populate method.")

        for generation in range(0, generations):
            # Seed random, which is used in gene mutation and chromosome
            # offspring.
            random.seed()

            # Select and multiply.
            self.select()
            self.multiply()

            yield generation + 1

    def select(self):
        """Evaluates each chromosome in the population to select the fittest of
        the population.
        """
        selected = []
        selection_count = int(self.size * self.selection_rate)

        # Evaluate each chromosome and store the fitness score for each result.
        for chromosome in self.chromosomes:
            fitness = self.evaluate(chromosome)
            selected.append((chromosome, fitness))

        # Get the selection based on sorting by the fitness score.
        sorted(selected, key=operator.itemgetter(1), reverse=True)
        selected = selected[:selection_count]

        selection = selected[0]
        if selection[1] > self.best_fit_fitness:
            self.best_fit_fitness = selection[1]
            self.best_fit = selection[0]

        # Create the new population.
        self.chromosomes = [s[0] for s in selected]

        return self.chromosomes

    def multiply(self):
        """Generate offspring until we're back to the right population size.
        """
        while len(self.chromosomes) < self.size:
            x = random.choice(self.chromosomes)
            y = random.choice(self.chromosomes)

            chromosome = Chromosome.offspring(x, y, self.crossover_rate, self.mutation_rate)

            self.chromosomes.append(chromosome)

    def evaluate(self, chromosome):
        return self.fitness_function(chromosome)

    def fitness(self, fitness_function):
        """Setter for the fitness function."""
        self.fitness_function = fitness_function

    def fittest(self):
        """Utility method for getting the best fit/fitness from the population
        at any given time.
        """
        return self.best_fit, self.best_fit_fitness


class PopulationException(Exception):
    pass
