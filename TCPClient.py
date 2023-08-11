import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tree way handshak managed by .connect
client.connect(('127.0.0.1', 9999))

client.send("Hello Server!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
#client.send("Bye!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))