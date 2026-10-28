# server.py
import socket, threading
def handle(c, addr):
  name = c.recv(1024).decode()
  while True:
    data = c.recv(1024)
    if not data:
      break
    print(name + ": " + data.decode())
  c.close()
s = socket.socket()
s.bind(("localhost", 5011))
s.listen()
print("Chat server running")
while True:
  c, addr = s.accept()
  threading.Thread(target=handle, args=(c, addr), daemon=True).start()
