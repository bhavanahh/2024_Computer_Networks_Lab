# server.py
import socket, json
s = socket.socket()
s.bind(("localhost", 5019))
s.listen(1)
c, addr = s.accept()
a = json.loads(c.recv(4096).decode())
result = [max(row) for row in a]
c.send(str(result).encode())
c.close()
s.close()
