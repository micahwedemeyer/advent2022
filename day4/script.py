from day4.elf_pair import ElfPair

input = open("input.txt").read().splitlines()
pairs = [ElfPair(line) for line in input]

overlap = len([p for p in pairs if p.has_overlap()])
print(overlap)
