from day5.platform import Platform


TEST_STR = "[M] [O]     [N]\n    [P] [Q]    \n 1   2   3   4 "

def test_parse():
    p = Platform(4, TEST_STR.splitlines())

    assert p.get_top(0) == "M"
    assert p.get_top(1) == "O"
    assert p.get_top(2) == "Q"
    assert p.get_top(3) == "N"


def test_parse_crate_row():
    row_str = "[M] [O]     [N]"
    row = Platform._parse_crate_row(row_str)

    assert row == ["M","O",None,"N"]
