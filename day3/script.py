from day3.rucksack import Rucksack
from functools import reduce

input = open("input.txt").read().splitlines()

sacks = [Rucksack(line) for line in input]
shared_sets = [r.shared_items() for r in sacks]
shared_items = reduce(lambda s1, s2: list(s1) + list(s2), shared_sets)

priority_sum = sum([i.priority() for i in shared_items])
print(priority_sum)
