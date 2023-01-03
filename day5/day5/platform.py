from collections import deque;

class Platform:

    def __init__(self, col_count, crate_str):
        self._stacks = [deque() for i in range(col_count)]
        self._parse_crate_str(crate_str)

    def get_top(self, col_idx):
        if col_idx >= len(self._stacks):
            return None

        col = self._stacks[col_idx]
        return col[0] if len(col) > 0 else None

    def _push(self, column, val):
        self._stacks[column].append(val)

    def _parse_crate_str(self, crate_str_lines):
        rows = [Platform._parse_crate_row(row_str) for row_str in crate_str_lines[:len(crate_str_lines) - 1]]
        for row in rows:
            # Lazy eval, which is why we need to encompass the generator in a comprehension
            [self._push(i, col_val) for (i, col_val) in enumerate(row) if col_val != None]

    @staticmethod
    def _parse_crate_row(row_str):
        col_strs = [row_str[i:i+4] for i in range(0,len(row_str),4)]
        return [i[1] if i.strip() != "" else None for i in col_strs]
