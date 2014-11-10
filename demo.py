#!/usr/bin/env python

from genetix.population import Population


CHARS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

p = Population()
p.populate(1000, {
  0: CHARS,
  1: CHARS,
  2: CHARS,
  3: CHARS,
  4: CHARS
})

@p.fitness
def hello(chromosome):
    target = "Hello"
    string = "".join([g.value for g in chromosome.genes])

    return sum([ch1 == ch2 for ch1, ch2 in zip(target, string)])

for g in p.evolve(1000):
    print p.fittest()