# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5023))
data, addr = s.recvfrom(4096)
text = data.decode()
clean = "".join(ch.lower() for ch in text if ch.isalnum())
result = f"Reverse={text[::-1]}\n" + ("Palindrome" if clean == clean[::-1] else "Not palindrome")
s.sendto(result.encode(), addr)
s.close()
