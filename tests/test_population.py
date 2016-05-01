import types
import unittest

from genetix.population import Population, PopulationException


class TestPopulation(unittest.TestCase):

    def setUp(self):
        self.population = Population()
        self.population.fitness(lambda c: sum([g.value for g in c.genes]))

    def test_init(self):
        self.assertIsInstance(self.population, Population)

    def test_evolve_failure(self):
        with self.assertRaises(PopulationException):
            for g in self.population.evolve(10):
                pass

    def test_evolve(self):
        blueprint = {'test': range(10)}
        self.population.populate(10, blueprint)

        results = list(self.population.evolve(10))
        self.assertTrue(len(results), 10)

    def test_populate(self):
        blueprint = {'test': range(10)}
        self.population.populate(10, blueprint)

        self.assertTrue(self.population.size == 10)
        self.assertTrue(len(self.population.chromosomes) == 10)

    def test_select(self):
        blueprint = {'test': range(100)}
        self.population.populate(100, blueprint)

        self.population.select()

        self.assertIsNotNone(self.population.best_fit)

    def test_multiply(self):
        # Populate
        blueprint = {'test': range(10)}
        self.population.populate(10, blueprint)

        # Reduce the population down to 2
        self.population.chromosomes = self.population.chromosomes[:2]

        # Call multiply and make sure we're back to the right population size.
        self.population.multiply()
        self.assertTrue(len(self.population.chromosomes) == 10)

    def test_fitness(self):
        self.population.fitness(lambda: 0)
        self.assertIsInstance(self.population.fitness_function, types.FunctionType)


if __name__ == '__main__':
    unittest.main()
