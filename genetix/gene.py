# -*- coding: utf-8 -*-

import random


class Gene(object):
    """The Gene class, which contains possible values, and can mutate."""

    def __init__(self, values):
        assert len(values)
        self.values = values

        self.mutate()

    def mutate(self):
        """
        :return: :class:`Gene <Gene>` object
        :rtype: genetix.gene.Gene
        """
        self.value = random.choice(self.values)
        return self

    def __repr__(self):
        return str(self.value)
