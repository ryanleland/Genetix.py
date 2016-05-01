import unittest

from genetix.chromosome import Chromosome


class TestChromosom(unittest.TestCase):

    def setUp(self):
        self.chromosome = Chromosome()

    def test_init(self):
        self.assertIsInstance(self.chromosome, Chromosome)

    def test_construct(self):
        chromosome = Chromosome.construct({'test': range(10)})

        self.assertTrue(len(chromosome.names) == 1)
        self.assertTrue(len(chromosome.genes) == 1)

    def test_offspring(self):
        blueprint = {'test': range(10)}

        x = Chromosome.construct(blueprint)
        y = Chromosome.construct(blueprint)
        chromosome = Chromosome.offspring(x, y, 1.0, 0.05)

        self.assertIsInstance(chromosome, Chromosome)
        self.assertTrue(len(chromosome) == 1)

    def test_len(self):
        chromosome = Chromosome.construct({'test': range(10)})
        self.assertTrue(len(chromosome) == 1)

    def test_repr(self):
        chromosome = Chromosome.construct({'test': [0]})
        self.assertTrue(str(chromosome) == 'test:0')


if __name__ == '__main__':
    unittest.main()
