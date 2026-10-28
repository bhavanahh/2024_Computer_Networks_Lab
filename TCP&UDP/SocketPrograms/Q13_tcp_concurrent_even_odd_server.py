# server.py
import socket, threading
def handle(c):
  n = int(c.recv(1024).decode())
  c.send(("Even" if n % 2 == 0 else "Odd").encode())
  c.close()
s = socket.socket()
s.bind(("localhost", 5012))
s.listen()
while True:
  c, addr = s.accept()
  threading.Thread(target=handle, args=(c,), daemon=True).start()
