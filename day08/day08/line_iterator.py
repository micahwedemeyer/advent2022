from io import TextIOWrapper, StringIO

class LineIterator:
    def __init__(self, input : TextIOWrapper):
        self._input = input
        self._row_count = 0
        self._column_count = 0

    def __iter__(self):
        self._line_reader = StringIO("")
        return self

    def __next__(self):
        c = self._line_reader.read(1)
        if c and not c == "\n":
            return int(c)

        next_line = self._input.readline().strip()
        if not next_line:
            raise StopIteration

        self._row_count += 1
        self._column_count = len(next_line)
        self._line_reader = StringIO(next_line)
        return int(self._line_reader.read(1))
