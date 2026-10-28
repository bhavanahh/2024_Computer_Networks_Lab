# client.py
import socket
s = socket.socket()
s.connect(("localhost", 5005))
nums = input("Enter integers separated by spaces: ")
s.send(nums.encode())
print(s.recv(1024).decode())
s.close()
