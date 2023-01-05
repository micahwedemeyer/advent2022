from day4.assignment import Assignment


def test_as_range():
    a = Assignment("22-66")
    r = a.as_range()
    assert 21 not in r
    assert 22 in r
    assert 66 in r
    assert 67 not in r

def test_fully_contains():
    a1 = Assignment("22-66")
    a2 = Assignment("33-44")
    a3 = Assignment("55-77")

    assert a1.fully_contains(a2)
    assert a2.fully_contains(a1) is False
    assert a1.fully_contains(a3) is False
