# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5012))
s.send(input("Enter integer: ").encode())
print(s.recv(1024).decode())
s.close()
