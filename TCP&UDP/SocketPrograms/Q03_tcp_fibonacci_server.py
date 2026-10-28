# server.py
import socket
s = socket.socket()
s.bind(("localhost", 5002))
s.listen(1)
c, addr = s.accept()
n = int(c.recv(1024).decode())
a, b, seq = 0, 1, []
for i in range(n):
  seq.append(a)
  a, b = b, a + b
c.send(str(seq).encode())
c.close()
s.close()
