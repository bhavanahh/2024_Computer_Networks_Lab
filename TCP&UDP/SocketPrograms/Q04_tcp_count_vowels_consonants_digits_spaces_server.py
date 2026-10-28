# server.py
import socket
s = socket.socket()
s.bind(("localhost", 5003))
s.listen(1)
c, addr = s.accept()
text = c.recv(4096).decode()
v = sum(ch.lower() in "aeiou" for ch in text)
con = sum(ch.isalpha() and ch.lower() not in "aeiou" for ch in text)
d = sum(ch.isdigit() for ch in text)
sp = sum(ch == " " for ch in text)
c.send(f"Vowels={v}, Consonants={con}, Digits={d}, Spaces={sp}".encode())
c.close()
s.close()
