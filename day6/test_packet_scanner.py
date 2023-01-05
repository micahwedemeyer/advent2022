import io
from day6.packet_scanner import PacketScanner

TEST_INPUT = "abcabcabcdab"

def test_bootstrap():
    # f = open('input.txt', 'r', encoding="utf-8")
    f = io.StringIO(TEST_INPUT)
    ps = PacketScanner(f)

    assert ps._pos == 4
    assert ps.window_str() == "abca"
    assert len(ps._marker_counts) == 3

def test_is_marker_window():
    f = io.StringIO(TEST_INPUT)
    ps = PacketScanner(f)

    assert ps.is_marker_window() is False

    ps = PacketScanner(io.StringIO("abcd"))
    assert ps.is_marker_window() is True

def test_advance():
    f = io.StringIO(TEST_INPUT)
    ps = PacketScanner(f)

    assert ps.window_str() == "abca"
    assert len(ps._marker_counts) == 3

    ps._advance()

    assert ps.window_str() == "bcab"
    assert len(ps._marker_counts) == 3


def test_find_packet_marker():
    f = io.StringIO(TEST_INPUT)
    ps = PacketScanner(f)

    n = ps.find_packet_marker()
    assert n == 10
