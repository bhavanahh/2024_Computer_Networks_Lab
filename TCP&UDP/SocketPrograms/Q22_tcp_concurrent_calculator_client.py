# client.py
import socket
a = input("First number: ")
op = input("Operator (+ - * /): ")
b = input("Second number: ")
s = socket.socket()
s.connect(("localhost", 5022))
s.send(f"{a} {op} {b}".encode())
print("Result:", s.recv(1024).decode())
s.close()
