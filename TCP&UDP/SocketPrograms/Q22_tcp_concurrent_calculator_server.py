# server.py
import socket, threading
def handle(c):
  a, op, b = c.recv(1024).decode().split()
  a, b = float(a), float(b)
  if op == "+": r = a + b
  elif op == "-": r = a - b
  elif op == "*": r = a * b
  elif op == "/": r = "Cannot divide by zero" if b == 0 else a / b
  else: r = "Invalid operator"
  c.send(str(r).encode())
  c.close()
s = socket.socket()
s.bind(("localhost", 5022))
s.listen()
while True:
  c, addr = s.accept()
  threading.Thread(target=handle, args=(c,), daemon=True).start()
