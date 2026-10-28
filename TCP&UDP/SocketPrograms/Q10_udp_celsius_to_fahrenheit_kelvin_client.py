# client.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Temperature in Celsius: ").encode(), ("localhost", 5009))
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
