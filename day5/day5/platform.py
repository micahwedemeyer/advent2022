from collections import deque;

class Platform:

    def __init__(self, crate_str, col_count = 9):
        self._stacks = [deque() for i in range(col_count)]
        self._parse_crate_str(crate_str.splitlines())

    def get_top(self, col_idx):
        if col_idx >= len(self._stacks):
            return None

        col = self._stacks[col_idx]
        return col[-1] if len(col) > 0 else None

    def move(self, move):
        for i in range(move.n()):
            v = self._pop(move.from_col())
            self._push(move.to_col(), v)

    def _push(self, column, val):
        self._stacks[column].append(val)

    def _pop(self, column):
        return self._stacks[column].pop()

    def _parse_crate_str(self, crate_str_lines):
        rows = [Platform._parse_crate_row(row_str) for row_str in crate_str_lines[:len(crate_str_lines) - 1]]

        # Push from bottom to top
        for row in reversed(rows):
            # Lazy eval, which is why we need to encompass the generator in a comprehension
            [self._push(i, col_val) for (i, col_val) in enumerate(row) if col_val != None]

    @staticmethod
    def _parse_crate_row(row_str):
        col_strs = [row_str[i:i+4] for i in range(0,len(row_str),4)]
        return [i[1] if i.strip() != "" else None for i in col_strs]

    # def __str__(self):
    #     row_count = max([len(s) for s in self._stacks])
    #     for height in range(row_count, 0):
    #         row = []
    #         for col_i in range(len(self._stacks)):
    #             if len(self._stacks[col_i] > height)
