from io import StringIO
from day08.forest import Forest

TEST_FOREST = """
30373
25512
65332
33549
35390
""".strip()

def test_input_read():
    f = Forest(StringIO(TEST_FOREST))
    f._process_input()
    assert f._array[0][0] == 3
    assert f._array[1][0] == 2
    assert f._array[1][3] == 1

def test_is_visible_in_row():
    row = [3,0,3,7,3]
    assert Forest._is_visible_in_row(row, 0) == True
    assert Forest._is_visible_in_row(row, 1) == False
    assert Forest._is_visible_in_row(row, 2) == False
    assert Forest._is_visible_in_row(row, 3) == True
    assert Forest._is_visible_in_row(row, 4) == True

def test_is_visible():
    f = Forest(StringIO(TEST_FOREST))
    f._process_input()

    assert f.is_visible(0,0) == True
    assert f.is_visible(0,1) == True
    assert f.is_visible(1,3) == False

def test_total_visible():
    f = Forest(StringIO(TEST_FOREST))
    f._process_input()

    assert f.total_visible() == 21
