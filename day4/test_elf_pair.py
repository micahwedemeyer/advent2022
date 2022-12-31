from day4.elf_pair import ElfPair


def test_has_overlap():
    ep1 = ElfPair("1-4,5-9")
    ep2 = ElfPair("3-6,5-8")

    assert ep1.has_overlap() == False
    assert ep2.has_overlap() == True

def test_get_overlap():
    ep1 = ElfPair("1-4,5-9")
    ep2 = ElfPair("3-6,5-8")

    assert ep1.get_overlap() == []
    assert ep2.get_overlap() == [5,6]

def test_has_full_overlap():
    ep1 = ElfPair("1-4,5-9")
    ep2 = ElfPair("3-6,5-8")
    ep3 = ElfPair("3-6,4-6")

    assert ep1.has_full_overlap() is False
    assert ep2.has_full_overlap() is False
    assert ep3.has_full_overlap() is True
