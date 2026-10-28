# server.py
import socket
from datetime import datetime
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5014))
data, addr = s.recvfrom(1024)
now = datetime.now()
result = now.strftime("Date: %d-%m-%Y, Day: %A, Time: %H:%M:%S")
s.sendto(result.encode(), addr)
s.close()
