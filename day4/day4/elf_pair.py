from day4.assignment import Assignment

class ElfPair:
    assignments = ()

    def __init__(self, assignment_str: str):
        parts = assignment_str.split(",")
        self.assignments = (Assignment(parts[0]), Assignment(parts[1]))

    def has_overlap(self):
        return len(self.get_overlap()) > 0

    def get_overlap(self):
        return [x for x in self.assignments[0].as_range() if x in self.assignments[1].as_range()]

    def has_full_overlap(self):
        return (self.assignments[0].fully_contains(self.assignments[1]) or
            self.assignments[1].fully_contains(self.assignments[0]))
