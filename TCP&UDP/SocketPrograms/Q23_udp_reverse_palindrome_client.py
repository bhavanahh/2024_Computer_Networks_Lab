# client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Enter string: ").encode(), ("localhost", 5023))
data, addr = s.recvfrom(4096)
print(data.decode())
s.close()
