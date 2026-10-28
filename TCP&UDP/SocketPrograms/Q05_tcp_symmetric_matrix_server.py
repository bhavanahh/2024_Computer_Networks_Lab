# server.py
import socket, json
s = socket.socket()
s.bind(("localhost", 5004))
s.listen(1)
c, addr = s.accept()
a = json.loads(c.recv(4096).decode())
ok = all(a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a)))
c.send(("Symmetric" if ok else "Not symmetric").encode())
c.close()
s.close()
