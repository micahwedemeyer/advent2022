from io import TextIOWrapper, StringIO, BufferedReader, RawIOBase, BytesIO
from day07.filesystem_builder import FilesystemBuilder
from day07.dir import Dir
from day07.fyle import Fyle
from anytree import RenderTree

TEST_FS = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def test_parsing():
    # f = BufferedReader(BytesIO(bytes(TEST_FS, "utf-8")))
    f = TextIOWrapper(StringIO(TEST_FS))
    fsb = FilesystemBuilder(f)
    # fsb._process_input()

def test_next_is_command():
    s = "$ yup"
    s2 = "nope"

    # assert FilesystemBuilder._next_is_command(BufferedReader(BytesIO(bytes(s, "utf-8")))) is True
    # assert FilesystemBuilder._next_is_command(BufferedReader(BytesIO(bytes(s2, "utf-8")))) is False
    assert FilesystemBuilder._line_is_command(s) is True
    assert FilesystemBuilder._line_is_command(s2) is False

def test_append_subdir():
    fsb = FilesystemBuilder(StringIO(TEST_FS))
    assert len(fsb._root.children) == 0

    fsb._parse_dir_line("dir a")

    assert len(fsb._root.children) == 1

def test_append_file():
    fsb = FilesystemBuilder(StringIO(TEST_FS))
    assert len(fsb._root.children) == 0

    fsb._parse_file_line("555 log.out")

    assert len(fsb._root.children) == 1
    assert fsb._root.children[0].name == "log.out"
    assert fsb._root.children[0].size == 555

def test_change_dir():
    f = StringIO(TEST_FS)
    fsb = FilesystemBuilder(f)

    fsb._parse_dir_line("dir a")
    fsb._parse_dir_line("dir b")

    print(RenderTree(fsb._root))
    assert len(fsb._root.children) == 2

    fsb._change_dir("a")
    assert fsb._cwd.name == "a"
    assert len(fsb._cwd.children) == 0

    fsb._change_dir("..")
    assert fsb._cwd.name == "/"
    assert len(fsb._root.children) == 2
