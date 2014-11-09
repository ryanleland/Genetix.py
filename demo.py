#!/usr/bin/env python

import random, math

from genetix.population import Population
from genetix.target import Target


class StringTarget(Target):

    def fitness(self, chromosome):
        targetVal = '';
        i = 0
        while i < chromosome.length():
            letter = 0
            for n in range(i, (i + 8)):
                letter = letter << 1
                letter = letter | chromosome.gene(i)
                i = i + 1
                
            targetVal = targetVal + chr(letter)
        
        chromosome.setFitness(float(self.hamming_distance(targetVal, self._value)))
        
        # Just for demo purposes
        print targetVal
        
    def hamming_distance(self, string1, string2):
        assert len(string1) == len(string2)
        return sum([ch1 != ch2 for ch1, ch2 in zip(string1, string2)])

pop = Population()
target = StringTarget("Hello World!")

pop.populate(1000, (12 * 8))

while pop.generation() < 3000: 
    pop.selection(target)
    
print pop.fittest().fitness()