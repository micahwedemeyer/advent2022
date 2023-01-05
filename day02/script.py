from day2.move import Move
from functools import reduce

lines = open('input.txt').read().splitlines()
moves = list(map(Move, lines))

sum_score = sum(map(lambda m: m.total_score(), moves))
print(sum_score)
