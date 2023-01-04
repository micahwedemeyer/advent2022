from day5.platform import Platform
from day5.move import Move

#     [O]
# [M] [P] [Q] [N]
#  1   2   3   4
TEST_STR = "    [O]        \n[M] [P] [Q] [N]\n 1   2   3   4 "

def test_parse():
    p = Platform(TEST_STR, 4)

    assert p.get_top(0) == "M"
    assert p.get_top(1) == "O"
    assert p.get_top(2) == "Q"
    assert p.get_top(3) == "N"


def test_parse_crate_row():
    row_str = "[M] [O]     [N]"
    row = Platform._parse_crate_row(row_str)

    assert row == ["M","O",None,"N"]


def test_pop():
    p = Platform(TEST_STR, 4)

    assert p.get_top(0) == "M"
    assert p.get_top(1) == "O"

    v = p._pop(0)
    p._pop(1)

    assert v == "M"
    assert p.get_top(0) == None
    assert p.get_top(1) == "P"

def test_move():
    p = Platform(TEST_STR, 4)

    assert p.get_top(0) == "M"
    assert p.get_top(1) == "O"

    m = Move("move 2 from 2 to 1")
    p.move(m)

    assert p.get_top(0) == "P"
    assert p.get_top(1) == None
