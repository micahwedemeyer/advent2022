from day3.compartment import Compartment
from functools import reduce

class Rucksack:
    def __init__(self, contents_str):
        halfway_point = len(contents_str) // 2
        self._compartments = [
            Compartment(contents_str[0 : halfway_point]),
            Compartment(contents_str[halfway_point : len(contents_str)])
        ]

    def compartments(self):
        return self._compartments.copy()

    def shared_items(self):
        return reduce(lambda s1, s2: s1 & s2, map(lambda c: c.as_set(), self._compartments))
