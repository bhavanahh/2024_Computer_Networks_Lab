# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5010))
data, addr = s.recvfrom(4096)
t = data.decode()
result = f"Upper={t.upper()}\nLower={t.lower()}\nReverse={t[::-1]}"
s.sendto(result.encode(), addr)
s.close()
