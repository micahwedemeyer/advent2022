from io import TextIOWrapper
from anytree import RenderTree, PreOrderIter
from day07.filesystem_builder import FilesystemBuilder
from day07.dir import Dir

# f = open('input.txt', 'r', encoding="utf-8")
# fs = FilesystemBuilder(f)
# fs._process_input()

with open('input.txt', 'r', encoding="utf-8") as f:
    fs = FilesystemBuilder(f)
    fs._process_input()
    # print(RenderTree(fs._root))

    all_dirs = [d for d in PreOrderIter(fs._root) if isinstance(d, Dir)]
    size_dirs = [d for d in all_dirs if d.sum_size() < 100000]

    print(sum([d.sum_size() for d in size_dirs]))
