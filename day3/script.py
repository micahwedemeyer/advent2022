from day3.rucksack import Rucksack
from functools import reduce

input = open("input.txt").read().splitlines()

sacks = [Rucksack(line) for line in input]

tri_groups = [sacks[i: i + 3] for i in range(0, len(sacks), 3)]


overlaps = [g[0].overlap_items(g[1], g[2]) for g in tri_groups]
s = sum(map(lambda s: list(s)[0].priority(), overlaps))

print(s)


# shared_sets = [r.shared_items() for r in sacks]
# shared_items = reduce(lambda s1, s2: list(s1) + list(s2), shared_sets)
#
# priority_sum = sum([i.priority() for i in shared_items])
# print(priority_sum)
