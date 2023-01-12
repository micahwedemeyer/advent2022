from anytree import RenderTree
from day07.dir import Dir
from day07.fyle import Fyle

def test_sum_size():
    p = Dir("parent")
    c1 = Dir("child1")
    c2 = Dir("child2")
    c3 = Dir("child1-1")

    p.append_subdir(c1)
    p.append_subdir(c2)
    c1.append_subdir(c3)

    p.append_file(Fyle(name="f1", size=100))
    c2.append_file(Fyle(name="f2", size=30))
    c3.append_file(Fyle(name="f3", size=5))

    print(RenderTree(p))
    assert len(p.children) == 3 # 2 dirs, 1 file
    assert p.sum_size() == 135
