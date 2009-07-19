class Target(object):
	def __init__(self, value):
		self._value = value

	def value(self):
		return self._value
		
	def setValue(self, value):
		self._value = value
		
	def fitness(self, chromosome):
		raise Exception, "Target not implemented."