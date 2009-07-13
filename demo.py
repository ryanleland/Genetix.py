import Population, Target

pop = Population.Population()
target = Target.Target()

pop.populate(2000, (12 * 8))

while pop.generation() < 1000: 
	pop.selection(target)
	
print pop.fittest().fitness()