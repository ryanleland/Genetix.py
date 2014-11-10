import random


class Gene(object):

    def __init__(self, values):
        self.values = values
        self.mutate()

    def mutate(self):
        assert len(self.values)
        self.value = random.choice(self.values)
        
        return self

    def __repr__(self):
        return str(self.value)