# server.py
import socket, os
s = socket.socket()
s.bind(("localhost", 5018))
s.listen(1)
c, addr = s.accept()
name = c.recv(1024).decode()
if os.path.isfile(name):
  with open(name, "rb") as f:
    content = f.read()
  c.sendall(f"OK|{len(content)}|".encode() + content)
else:
  c.send(b"ERROR|File not found")
c.close()
s.close()
