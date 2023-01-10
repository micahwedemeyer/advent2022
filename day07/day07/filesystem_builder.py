import re
from io import TextIOWrapper, BufferedReader
from day07.dir import Dir
from day07.fyle import Fyle
from anytree import Node, RenderTree

class FilesystemBuilder:
    DIR_PATTERN = "dir (\\w+)"
    FILE_PATTERN = "(\\d+) (.+)$"

    def __init__(self, terminal_stream: TextIOWrapper):
        self._terminal_stream = terminal_stream

        self._root = Dir("/")
        self._cwd = self._root

    def _process_input(self):
        while(self._terminal_stream.readable()):
            input_line = self._terminal_stream.readline()
            if (FilesystemBuilder._line_is_command(input_line)):
                self._run_command(input_line)
            else:
                self._parse_output_line(input_line)

    def _line_is_command(line : str) -> bool:
        return len(line) > 0 and line[0] == "$"

    def _run_command(self, input_line : str):
        print("cmd: " + input_line)

    def _parse_output_line(self, input_line : str):
        print("out: " + input_line)

    def _parse_dir_line(self, input_line: str):
        dir_name = re.match(FilesystemBuilder.DIR_PATTERN, input_line).groups()[0]
        self._cwd.append_subdir(dir_name)

    def _parse_file_line(self, input_line: str):
        file_size, file_name = re.match(FilesystemBuilder.FILE_PATTERN, input_line).groups()
        self._cwd.append_file(Fyle(name=file_name, size=int(file_size)))
