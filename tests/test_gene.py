import unittest

from genetix.gene import Gene


class TestGene(unittest.TestCase):

    def setUp(self):
        self.gene = Gene([0])

    def test_constructor(self):
        self.assertIsInstance(self.gene, Gene)

    def test_values_len_assertion(self):
        with self.assertRaises(AssertionError) as context:
            gene = Gene([])

    def test_mutate(self):
        values = range(100)

        gene = Gene(values)
        gene.mutate()

        self.assertTrue(gene.value in values)

    def test_repr(self):
        self.assertEquals(str(self.gene), '0')

if __name__ == '__main__':
    unittest.main()
