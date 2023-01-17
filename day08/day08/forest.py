from io import TextIOWrapper
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
