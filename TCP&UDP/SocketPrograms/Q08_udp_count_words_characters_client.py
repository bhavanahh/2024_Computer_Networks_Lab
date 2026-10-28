# client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Enter sentence: ").encode(), ("localhost", 5007))
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
