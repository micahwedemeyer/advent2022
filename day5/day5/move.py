import re

class Move:
    _PATTERN = "move (\\d+) from (\\d+) to (\\d+)"

    def __init__(self, move_str):
        self._move = Move._parse_move_str(move_str)

    def from_col(self):
        return self._move[1]

    def to_col(self):
        return self._move[2]

    def n(self):
        return self._move[0]

    # move 3 from 2 to 9
    def _parse_move_str(move_str):
        m = re.search(Move._PATTERN, move_str)
        return tuple([int(n) for n in m.groups()])
