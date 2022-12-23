from day3.item import Item

def test_priority():
    a1 = Item("a")
    assert a1.priority() == 1

    a2 = Item("A")
    assert a2.priority() == 27

    l2 = Item("L")
    assert l2.priority() == 38

    p1 = Item("p")
    assert p1.priority() == 16

    p2 = Item("P")
    assert p2.priority() == 42

def test_equals():
    assert Item("a") == Item("a")
    assert Item("A") != Item("a")
    assert Item("b") != Item("a")

def test_hash():
    assert hash(Item("a")) == hash(Item("a"))
    assert hash(Item("B")) == hash(Item("B"))
