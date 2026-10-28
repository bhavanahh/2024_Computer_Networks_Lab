# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5008))
data, addr = s.recvfrom(1024)
n = int(data.decode())
if n < 2:
  result = "Neither prime nor composite"
else:
  prime = all(n % i != 0 for i in range(2, int(n**0.5) + 1))
  result = "Prime" if prime else "Composite"
s.sendto(result.encode(), addr)
s.close()
