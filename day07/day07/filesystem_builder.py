import re
from io import TextIOWrapper, BufferedReader
from day07.dir import Dir
from day07.fyle import Fyle
from anytree import Node, RenderTree

class FilesystemBuilder:
    DIR_PATTERN = "dir (\\w+)"
    FILE_PATTERN = "(\\d+) (.+)$"
    CD_PATTERN = "\\$ cd (.*)$"

    def __init__(self, terminal_stream: TextIOWrapper):
        self._terminal_stream = terminal_stream

        self._root = Dir("/")
        self._cwd = self._root

    def _process_input(self):
        for input_line in self._terminal_stream:
            if (FilesystemBuilder._line_is_command(input_line)):
                self._run_command(input_line)
            else:
                self._parse_output_line(input_line)

    def _line_is_command(line : str) -> bool:
        return len(line) > 0 and line[0] == "$"

    def _run_command(self, input_line : str):
        m = re.match(FilesystemBuilder.CD_PATTERN, input_line)
        if m:
            self._change_dir(m.groups()[0])
        elif input_line == "$ ls":
            self._ls()

    def _change_dir(self, dir : str):
        if dir == "..":
            self._cwd = self._cwd.parent
        elif dir == "/":
            self._cwd = self._root
        else:
            self._cwd = [c for c in self._cwd.children if c.name == dir][0]

    def _ls(self):
        None # no-op

    def _parse_output_line(self, input_line : str):
        if re.match(FilesystemBuilder.DIR_PATTERN, input_line):
            self._parse_dir_line(input_line)
        elif re.match(FilesystemBuilder.FILE_PATTERN, input_line):
            self._parse_file_line(input_line)

    def _parse_dir_line(self, input_line: str):
        dir_name = re.match(FilesystemBuilder.DIR_PATTERN, input_line).groups()[0]
        self._cwd.append_subdir(dir_name)

    def _parse_file_line(self, input_line: str):
        file_size, file_name = re.match(FilesystemBuilder.FILE_PATTERN, input_line).groups()
        self._cwd.append_file(Fyle(name=file_name, size=int(file_size)))
