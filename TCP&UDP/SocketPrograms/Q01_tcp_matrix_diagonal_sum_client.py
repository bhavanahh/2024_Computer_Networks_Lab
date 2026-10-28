# client.py
import socket, json, random
n = int(input("Enter N: "))
a = [[random.randint(1, 50) for j in range(n)] for i in range(n)]
print("Matrix:", a)
s = socket.socket()
s.connect(("localhost", 5000))
s.send(json.dumps(a).encode())
print("Diagonal sum:", s.recv(1024).decode())
s.close()
