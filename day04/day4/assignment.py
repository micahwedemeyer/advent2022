class Assignment:
    low = -1
    high = -1

    def __init__(self, assignment_str: str):
        self.__parse_assignment(assignment_str)


    def as_range(self):
        return range(self.low, self.high)

    def __parse_assignment(self, assignment_str: str):
        parts = assignment_str.split("-")
        self.low = int(parts[0])
        self.high = int(parts[1]) + 1

    def fully_contains(self, assignment2) -> bool:
        r1 = self.as_range()
        r2 = assignment2.as_range()
        return len([x for x in r2 if x not in r1]) == 0
