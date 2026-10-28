# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5003))
s.send(input("Enter sentence: ").encode())
print(s.recv(1024).decode())
s.close()
