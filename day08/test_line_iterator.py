from io import StringIO
from day08.line_iterator import LineIterator

def test_line_iterator():
    s = "4321\n1234\n9876\n"
    li = LineIterator(StringIO(s))
    result = [c for c in li]

    assert result[0] == 4
    assert result[4] == 1
    assert li._column_count == 4
    assert li._row_count == 3
