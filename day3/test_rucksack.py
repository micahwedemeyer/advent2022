from day3.rucksack import Rucksack
from day3.item import Item


# def test_compartments():
#     r = Rucksack("abcdXYZA")
#     c2 = r.compartments()[1]
#     assert c2.as_str() == "XYZA"
#
#
# def test_shared_items():
#     r = Rucksack("abcdXYZA")
#     shared = r.shared_items()
#     assert len(shared) == 0
#
#     r = Rucksack("abXdXYZA")
#     shared = r.shared_items()
#     assert len(shared) == 1
#     assert list(shared)[0] == Item("X")
#
#     r = Rucksack("abcddcba")
#     shared = r.shared_items()
#     assert len(shared) == 4
#     assert Item("a") in shared
#     assert Item("b") in shared
#     assert Item("c") in shared
#     assert Item("d") in shared

def test_overlap_items():
    r1 = Rucksack("abcdXYZA")
    r2 = Rucksack("ghjkGHJK")
    r3 = Rucksack("qwerQWER")

    overlap = r1.overlap_items(r2, r3)
    assert len(overlap) == 0

    r1 = Rucksack("abcQXYZA")
    r2 = Rucksack("ghjQGHJK")
    r3 = Rucksack("qwerQWER")

    overlap = r1.overlap_items(r2, r3)
    assert len(overlap) == 1
    assert Item("Q") in overlap
