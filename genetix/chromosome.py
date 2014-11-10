import random

from gene import Gene


class Chromosome(object):

    def __init__(self, names=[], genes=[]):
        self.names = names
        self.genes = genes

    def construct(self, blueprint):
        self.names = []
        self.genes = []

        for name, values in blueprint.items():
            self.names.append(name)
            self.genes.append(Gene(values))

    def offspring(self, x, y, crossover_rate, mutation_rate):
        self.names = x.names
        self.genes = []

        gene_count = int((len(x) + len(y)) / 2)
        crossover = random.randrange(0, int(gene_count * crossover_rate))

        # Populate with X
        for i in range(0, crossover):
            self.genes.append(x.genes[i])
            
        # Populate with Y
        for i in range(crossover, gene_count):
            self.genes.append(y.genes[i])

        mutation = int(10000 * mutation_rate)
        for gene in self.genes:
            if mutation > random.randrange(0, 10000):
                gene.mutate()

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
