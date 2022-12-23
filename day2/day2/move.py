from enum import Enum

class Move:
    class Outcome(Enum):
        LOSE = 1
        WIN = 2
        DRAW = 3

    SHAPE_SCORES = {"X" : 1, "Y": 2, "Z": 3}

    OUTCOME_SCORES = {
        Outcome.LOSE: 0,
        Outcome.DRAW: 3,
        Outcome.WIN: 6
    }

    OUTCOMES = {
        "AX" : Outcome.DRAW,
        "AY" : Outcome.WIN,
        "AZ" : Outcome.LOSE,
        "BX" : Outcome.LOSE,
        "BY" : Outcome.DRAW,
        "BZ" : Outcome.WIN,
        "CX" : Outcome.WIN,
        "CY" : Outcome.LOSE,
        "CZ" : Outcome.DRAW
    }

    def __init__(self, move_str):
        self.move_str = move_str

    def score(self):
        return None

    def shape_score(self):
        return self.SHAPE_SCORES[self.my_shape()]

    def my_shape(self):
        return self.move_str[2]

    def opponent_shape(self):
        return self.move_str[0]

    def outcome(self):
        key = self.opponent_shape() + self.my_shape()
        return self.OUTCOMES[key]

    def outcome_score(self):
        return self.OUTCOME_SCORES[self.outcome()]

    def total_score(self):
        return self.shape_score() + self.outcome_score()
