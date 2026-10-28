# client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"date", ("localhost", 5014))
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
