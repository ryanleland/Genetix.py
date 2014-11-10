Genetix.py
==========

Created based on the need for an easy to use and understand GA library.

Installation
------------

	$ pip install https://github.com/ryanleland/Genetix.py

Usage
-----

There are a few simple steps to usage that is explained in the `demo.py` file in the root of the project. Please feel free to run it, and change values to see how it changes the outcome.

1. Import and instantiate a `Population` class.

	from genetix.population import Population
	population = Population()

2. Set the population size and a blueprint for the chromosome.
	- Note that each item in the dictionary represents a named Gene, which can have any possibility based on a provided range, or list.

	population.populate(10, {
	  0: range(0, 100),
	  1: range(0, 100),
	  2: range(0, 100),
	  3: range(0, 100),
	  4: range(0, 100),
	  5: range(0, 100),
	  6: range(0, 100),
	  7: range(0, 100),
	  8: range(0, 100),
	  9: range(0, 100)
	})

3. Decorate a function to use test fitness.
	
	@population.fitness
	def max(chromosome):
	    # Return a sum of all the gene values.
	    return sum([g.value for g in chromosome.genes])

4. Evolve the population.
	
	for g in population.evolve(100):
	    print population.fittest()

