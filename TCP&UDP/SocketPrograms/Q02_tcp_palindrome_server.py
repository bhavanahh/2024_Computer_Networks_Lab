# server.py
import socket
s = socket.socket()
s.bind(("localhost", 5001))
s.listen(1)
c, addr = s.accept()
word = c.recv(1024).decode()
result = "Palindrome" if word.lower() == word[::-1].lower() else "Not palindrome"
c.send(result.encode())
c.close()
s.close()
