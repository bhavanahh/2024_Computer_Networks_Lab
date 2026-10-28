# server.py
import socket, json
s = socket.socket()
s.bind(("localhost", 5020))
s.listen(1)
c, addr = s.accept()
a = json.loads(c.recv(4096).decode())
n = len(a)
diag = all(a[i][j] == 0 for i in range(n) for j in range(n) if i != j)
upper = all(a[i][j] == 0 for i in range(n) for j in range(i))
lower = all(a[i][j] == 0 for i in range(n) for j in range(i+1, n))
if diag:
  result = "Diagonal"
elif upper:
  result = "Upper triangular"
elif lower:
  result = "Lower triangular"
else:
  result = "Neither"
c.send(result.encode())
c.close()
s.close()
