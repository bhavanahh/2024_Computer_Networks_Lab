# server.py
import socket
from datetime import datetime
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5013))
while True:
  data, addr = s.recvfrom(1024)
  s.sendto(datetime.now().strftime("%Y-%m-%d %A %H:%M:%S").encode(), addr)
