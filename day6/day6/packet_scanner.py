from io import TextIOWrapper
from collections import deque


# There are simpler ways to do this, but I believe this is an O(1) solution
# for advancing the window and will not get slower as window size or input
# size increases
class PacketScanner:
    WINDOW_SIZE = 14

    def __init__(self, input : TextIOWrapper):
        self._input = input
        self._window = deque()
        self._marker_counts = {}
        self._pos = 0
        self._bootstrap()

    def _bootstrap(self):
        [self._window.append(c) for c in self._input.read(PacketScanner.WINDOW_SIZE)]
        [self._mark(c) for c in self._window]
        self._pos = PacketScanner.WINDOW_SIZE

    def find_packet_marker(self):
        while not self.is_marker_window():
            self._advance()

        return self._pos

    def is_marker_window(self) -> bool:
        return len(self._marker_counts) == PacketScanner.WINDOW_SIZE

    def window_str(self) -> str:
        return "".join(self._window)

    def _advance(self):
        self._pos += 1
        c = self._window.popleft()
        self._unmark(c)
        c = self._input.read(1)
        self._window.append(c)
        self._mark(c)

    def _mark(self, c):
        if c in self._marker_counts:
            self._marker_counts[c] += 1
        else:
            self._marker_counts[c] = 1

    def _unmark(self, c):
        self._marker_counts[c] -= 1
        if self._marker_counts[c] == 0:
            self._marker_counts.pop(c)
