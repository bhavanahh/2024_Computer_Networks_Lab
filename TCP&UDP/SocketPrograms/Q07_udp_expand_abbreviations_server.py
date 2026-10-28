# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5006))
text, addr = s.recvfrom(4096)
words = {"u":"you", "ur":"your", "pls":"please", "thx":"thanks", "bcz":"because", "msg":"message"}
result = " ".join(words.get(w.lower(), w) for w in text.decode().split())
s.sendto(result.encode(), addr)
s.close()
