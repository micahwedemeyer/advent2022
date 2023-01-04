from day5.move import Move

def test_move():
    m = Move("move 18 from 7 to 4")

    assert m.n() == 18
    assert m.from_col() == 6
    assert m.to_col() == 3
