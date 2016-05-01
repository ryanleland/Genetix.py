#!/usr/bin/env python

import string
from fuzzywuzzy import fuzz

# Import the population.
from genetix.population import Population


# Create a population.
population = Population(selection_rate=0.4, crossover_rate=1.0, mutation_rate=0.12)

# Set the population size and a blueprint for the chromosome.
# Note that each item in the dictionary represents a named Gene, which can have
# any possibility based on a provided range, or list.
values = string.letters + ",! "
population.populate(2500, {
  0:  values,
  1:  values,
  2:  values,
  3:  values,
  4:  values,
  5:  values,
  6:  values,
  7:  values,
  8:  values,
  9:  values,
  10: values,
  11: values,
  12: values
})

# Decorate a function to use test fitness.
@population.fitness
def max(chromosome):
    string = "".join([g.value for g in chromosome.genes])
    target = "Hello, World!"

    return fuzz.QRatio(string, target)

# Evolve for 100 generations.
# The method is a generator to make it easier to do work after each generation.
for g in population.evolve(10000):
    # The 'fittest()' method will return the best chromosome as determined by
    # the fitness method.
    chromosome, score = population.fittest()

    if chromosome:
        string = "".join([g.value for g in chromosome.genes])
        print string, score
