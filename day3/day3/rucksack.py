from day3.compartment import Compartment
from functools import reduce

class Rucksack:
    def __init__(self, contents_str):
        # halfway_point = len(contents_str) // 2
        # self._compartments = [
        #     Compartment(contents_str[0 : halfway_point]),
        #     Compartment(contents_str[halfway_point : len(contents_str)])
        # ]

        # Part 2 we'll use a single compartment
        self._compartments = [Compartment(contents_str)]

    def compartments(self):
        return self._compartments.copy()

    # def shared_items(self):
    #     return reduce(lambda s1, s2: s1 & s2, map(lambda c: c.as_set(), self._compartments))

    def overlap_items(self, *other_sacks):
        sets = [r.compartments()[0].as_set() for r in [self] + list(other_sacks)]
        return reduce(lambda s1, s2: s1 & s2, sets)
