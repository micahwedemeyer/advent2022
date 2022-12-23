from functools import reduce
class Elf:
    calorie_stack = []

    def __init__(self, calorie_stack = []):
        lines = calorie_stack.splitlines()
        self.calorie_stack = list(map(int, lines))

    def get_sum_calories(self):
        return reduce(lambda x,y: x+y, self.calorie_stack, 0)
