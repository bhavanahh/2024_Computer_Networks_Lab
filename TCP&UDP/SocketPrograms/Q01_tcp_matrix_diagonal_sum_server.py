# server.py
import socket, json
s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)
c, addr = s.accept()
a = json.loads(c.recv(4096).decode())
total = sum(a[i][i] for i in range(len(a)))
c.send(str(total).encode())
c.close()
s.close()
