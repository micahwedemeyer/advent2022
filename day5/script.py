from day5.move import Move
from day5.platform import Platform

(plat_str,move_str) = open("input.txt").read().split("\n\n")

platform = Platform(plat_str)
moves = [Move(m) for m in move_str.splitlines()]
[platform.move(m) for m in moves]
[print(platform.get_top(i)) for i in range(9)]
