# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5007))
text, addr = s.recvfrom(4096)
text = text.decode()
result = f"Words={len(text.split())}, Characters={len(text)}"
s.sendto(result.encode(), addr)
s.close()
