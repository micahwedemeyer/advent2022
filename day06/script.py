from day6.packet_scanner import PacketScanner

f = open('input.txt', 'r', encoding="utf-8")
ps = PacketScanner(f)

n = ps.find_packet_marker()
print(n)
