import random, math

class Target:
	def __init__(self):
		self._value = "Hello World!"

	def value(self):
		return self._value
		
	def setValue(self, value):
		self._value = value

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
		
		distance = 0.0;
		for n in range(0, len(self._value)):
			distance = distance + math.fabs(ord(targetVal[n]) - ord(self._value[n]))
		
		chromosome.setFitness(float(distance))
		
		print targetVal