import socket

    # Create Socket Client #
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello Server!  I'm UDP".encode('utf-8'), ('192.168.1.115', 9999))
client.sendto("BYE".encode('utf-8'), ('192.168.1.115', 9999))
print(client.recvfrom(1024)[0].decode('utf-8'))
