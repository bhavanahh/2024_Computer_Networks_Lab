# Matrix Classification Using Socket Programming

## Aim
To implement client-server communication using Python socket programming and identify the type of a square matrix.

## client.py

```python
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5060))

n = int(input("Enter the order of matrix: "))
matrix = []

print("Enter the elements of matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nMatrix:")

for row in matrix:
    print(*row)

data = pickle.dumps((n, matrix))
s.send(data)

result = s.recv(1024).decode()
print("Matrix type:", result)

s.close()
```

## server.py

```python
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5060))
s.listen(1)

print("Server is waiting for connection...")

conn, addr = s.accept()
print("Connected by:", addr)

data = pickle.loads(conn.recv(4096))
n, matrix = data

print("Received matrix of order", n, "from client:")

for row in matrix:
    print(*row)

upper = True
lower = True
diagonal = True

for i in range(n):
    for j in range(n):
        if i < j and matrix[i][j] != 0:
            lower = False
        if i > j and matrix[i][j] != 0:
            upper = False
        if i != j
