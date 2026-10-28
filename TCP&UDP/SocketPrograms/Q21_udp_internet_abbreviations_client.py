# client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Enter sentence: ").encode(), ("localhost", 5021))
data, addr = s.recvfrom(4096)
print(data.decode())
s.close()
