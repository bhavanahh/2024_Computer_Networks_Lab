# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5002))
s.send(input("Enter N: ").encode())
print("Fibonacci:", s.recv(4096).decode())
s.close()
