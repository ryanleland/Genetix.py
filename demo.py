from Population import Population
from StringTarget import StringTarget

pop = Population()
target = StringTarget("Hello World!")

pop.populate(1000, (12 * 8))

while pop.generation() < 3000: 
	pop.selection(target)
	
print pop.fittest().fitness()