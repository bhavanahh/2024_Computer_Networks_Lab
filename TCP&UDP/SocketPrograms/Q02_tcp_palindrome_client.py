# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5001))
s.send(input("Enter a string: ").encode())
print(s.recv(1024).decode())
s.close()
