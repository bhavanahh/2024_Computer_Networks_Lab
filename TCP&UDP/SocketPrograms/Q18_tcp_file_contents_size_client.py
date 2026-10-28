# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5018))
s.send(input("Filename on server: ").encode())
data = b""
while True:
  part = s.recv(4096)
  if not part:
    break
  data += part
print(data.decode(errors="replace"))
s.close()
