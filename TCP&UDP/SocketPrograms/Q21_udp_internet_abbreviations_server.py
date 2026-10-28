# server.py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 5021))
data, addr = s.recvfrom(4096)
words = {"tbh":"to be honest", "ig":"I guess", "tbf":"to be fair",
  "atm":"at the moment", "irl":"in real life", "lol":"laughing out loud",
  "asap":"as soon as possible", "omg":"oh my god", "ttyl":"talk to you later",
  "idk":"I do not know", "nvm":"never mind"}
result = " ".join(words.get(w.lower(), w) for w in data.decode().split())
s.sendto(result.encode(), addr)
s.close()
