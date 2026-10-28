# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5009))
data, addr = s.recvfrom(1024)
c = float(data.decode())
f = c * 9/5 + 32
k = c + 273.15
s.sendto(f"Fahrenheit={f:.2f}, Kelvin={k:.2f}".encode(), addr)
s.close()
