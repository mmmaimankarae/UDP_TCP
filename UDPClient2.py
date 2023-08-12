import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("This is New Client!".encode('utf-8'), ('192.168.60.84', 9999))
print(client.recvfrom(1024)[0].decode('utf-8'))
