from elf import Elf

def _read_input():
    f = open('input.txt')
    return f.read()

def _chunk_stacks(input):
    return input.split("\n\n")


input = _read_input()
stacks = _chunk_stacks(input)
full_stacks = (stack for stack in stacks if len(stack) > 0)

elves = map(Elf, full_stacks)
sorted_elves = sorted(elves, key = lambda e: e.get_sum_calories(), reverse = True)

highest_3 = sorted_elves[:3]
s = sum(map(lambda e: e.get_sum_calories(), highest_3))
print(s)
