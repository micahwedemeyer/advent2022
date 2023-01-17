from io import TextIOWrapper
from functools import reduce
import numpy as np
from day08.line_iterator import LineIterator

class Forest:
    @staticmethod
    def _is_visible_in_row(row, i):
        if i == 0 or i == len(row) - 1:
            return True

        x = row[i]
        # Shrink a digit so we can use max() and not get caught by equal
        # height trees
        adj_x = x - 1
        return (max(adj_x, max(row[:i])) == adj_x) or (max(adj_x, max(row[i+1:])) == adj_x)

    @staticmethod
    def _scenic_score_in_row(row, i):
        x = row[i]
        l_slice = np.flip(row[:i])
        r_slice = row[i+1:]
        return (Forest._scenic_score_in_slice(l_slice, x), Forest._scenic_score_in_slice(r_slice, x))


    def _scenic_score_in_slice(slice, x):
        # Are we at the edge? Then the score is 1
        if len(slice) == 0:
            return 1

        blocker_idxs = [i for (i, v) in enumerate(slice) if v >= x]

        score = -1
        if len(blocker_idxs) == 0:
            return len(slice)
        else:
            return min(blocker_idxs) + 1

    def __init__(self, input_stream : TextIOWrapper):
        self._input_stream = input_stream

    def _process_input(self):
        line_iterator = LineIterator(self._input_stream)
        self._array = np.fromiter(line_iterator, np.int8)
        self._array = np.reshape(self._array, (line_iterator._row_count, line_iterator._column_count))

    def is_visible(self, row_i, col_i):
        if row_i == 0 or row_i == len(self._array):
            return True

        row = self._array[row_i,:]
        col = self._array[:,col_i]
        return (Forest._is_visible_in_row(row, col_i) or Forest._is_visible_in_row(col, row_i))

    def total_visible(self):
        row_n = len(self._array)
        col_n = len(self._array[0])
        sum_visible = 0
        for row_i in range(row_n):
            row_sum = len([col_i for col_i in range(col_n) if self.is_visible(row_i, col_i)])
            sum_visible += row_sum

        return sum_visible

    def scenic_score(self, row_i, col_i):
        row = self._array[row_i,:]
        col = self._array[:,col_i]
        t1 = Forest._scenic_score_in_row(row, col_i)
        t2 = Forest._scenic_score_in_row(col, row_i)

        l = list(t1) + list(t2)
        return reduce(lambda x,y: x*y, l)

    def best_scenic_score(self):
        row_n = len(self._array)
        col_n = len(self._array[0])

        best_score = -1
        for row_i in range(row_n):
            for col_i in range(col_n):
                best_score = max(best_score, self.scenic_score(row_i, col_i))

        return best_score
