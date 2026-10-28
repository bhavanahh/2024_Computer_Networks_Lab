# server.py
import socket
s = socket.socket()
s.bind(("localhost", 5005))
s.listen(1)
c, addr = s.accept()
nums = list(map(int, c.recv(4096).decode().split()))
c.send(f"Largest={max(nums)}, Smallest={min(nums)}, Average={sum(nums)/len(nums):.2f}".encode())
c.close()
s.close()
