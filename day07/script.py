from io import TextIOWrapper
from anytree import RenderTree, PreOrderIter
from day07.filesystem_builder import FilesystemBuilder
from day07.dir import Dir

# f = open('input.txt', 'r', encoding="utf-8")
# fs = FilesystemBuilder(f)
# fs._process_input()

TOTAL_SIZE = 70000000
REQUIRED_SPACE = 30000000


with open('input.txt', 'r', encoding="utf-8") as f:
    fs = FilesystemBuilder(f)
    fs._process_input()
    # print(RenderTree(fs._root))

    total_used = fs._root.sum_size()
    total_unused = TOTAL_SIZE - total_used
    min_to_delete = REQUIRED_SPACE - total_unused

    print(f'Total size: {TOTAL_SIZE}')
    print(f'Total used: {total_used}')
    print(f'Total unused: {total_unused}')
    print(f'Min to delete: {min_to_delete}')

    smalls = [d for d in PreOrderIter(fs._root) if isinstance(d, Dir) and d.sum_size() >= min_to_delete]
    smalls.sort(key = lambda d: d.sum_size())

    print(smalls[0].sum_size())
