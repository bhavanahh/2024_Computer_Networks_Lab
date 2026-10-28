# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5011))
s.send(input("Username: ").encode())
while True:
  msg = input("Message (quit to stop): ")
  if msg.lower() == "quit":
    break
  s.send(msg.encode())
s.close()
