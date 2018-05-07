# -*- coding: utf-8 -*-

import random

from genetix.gene import Gene


class Chromosome(object):
    """The base Chromosome class, which is a container for genes, and handles
    mutation via the offspring method.
    """

    def __init__(self, names=[], genes=[]):
        self.names = names
        self.genes = genes

    @classmethod
    def construct(cls, blueprint):
        names = []
        genes = []

        for name, values in blueprint.items():
            names.append(name)
            genes.append(Gene(values))

        return cls(names, genes)

    @classmethod
    def offspring(cls, x, y, crossover_rate, mutation_rate):
        assert len(x) == len(y)

        genes = []
        gene_count = len(x)

        # Calculate mutation and crossover
        mutation = int(10000 * mutation_rate)
        crossover = random.randrange(0, int(gene_count * crossover_rate))

        # Populate with X
        for i in range(0, crossover):
            genes.append(x.genes[i])

        # Populate with Y
        for i in range(crossover, gene_count):
            genes.append(y.genes[i])

        for gene in genes:
            if mutation > random.randrange(0, 10000):
                gene.mutate()

        return cls(x.names, genes)

    def get_gene(self, index):
        return self.genes[index]

    def set_gene(self, index, gene):
        self.genes[index] = value

    def mutate_gene(self, index):
        self.genes[index].mutate()

    def __len__(self):
        return len(self.genes)

    def __repr__(self):
        return "\t".join(["%s:%s" % (name, gene) for name, gene in zip(self.names, self.genes)])
