# client.py
import socket, json
n = int(input("Enter N: "))
a = []
for i in range(n):
  a.append(list(map(int, input("Enter row: ").split())))
s = socket.socket()
s.connect(("localhost", 5020))
s.send(json.dumps(a).encode())
print(s.recv(1024).decode())
s.close()
