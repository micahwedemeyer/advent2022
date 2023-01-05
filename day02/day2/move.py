from enum import Enum

class Move:
    class Outcome(Enum):
        LOSE = 1
        WIN = 2
        DRAW = 3

    SHAPE_SCORES = {"A" : 1, "B": 2, "C": 3}

    DESIRED_OUTCOMES = {
        "X" : Outcome.LOSE,
        "Y" : Outcome.DRAW,
        "Z" : Outcome.WIN
    }

    OUTCOME_SCORES = {
        Outcome.LOSE: 0,
        Outcome.DRAW: 3,
        Outcome.WIN: 6
    }

    OUTCOMES = {
        "AA" : Outcome.DRAW,
        "AB" : Outcome.WIN,
        "AC" : Outcome.LOSE,
        "BA" : Outcome.LOSE,
        "BB" : Outcome.DRAW,
        "BC" : Outcome.WIN,
        "CA" : Outcome.WIN,
        "CB" : Outcome.LOSE,
        "CC" : Outcome.DRAW
    }

    RESPONSES = {
        ("A", Outcome.LOSE) : "C",
        ("A", Outcome.DRAW) : "A",
        ("A", Outcome.WIN) : "B",
        ("B", Outcome.LOSE) : "A",
        ("B", Outcome.DRAW) : "B",
        ("B", Outcome.WIN) : "C",
        ("C", Outcome.LOSE) : "B",
        ("C", Outcome.DRAW) : "C",
        ("C", Outcome.WIN) : "A",
    }

    def __init__(self, move_str):
        self.move_str = move_str

    def score(self):
        return None

    def shape_score(self):
        return self.SHAPE_SCORES[self.my_shape()]

    def desired_outcome(self):
        return self.DESIRED_OUTCOMES[self.move_str[2]]

    def my_shape(self):
        key = (self.opponent_shape(), self.desired_outcome())
        return self.RESPONSES[key]

    def opponent_shape(self):
        return self.move_str[0]

    def outcome(self):
        return self.desired_outcome()

    def outcome_score(self):
        return self.OUTCOME_SCORES[self.outcome()]

    def total_score(self):
        return self.shape_score() + self.outcome_score()
