import socket

    # Create Socket Client #
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tree way handshak managed by .connect
client.connect(('192.168.1.115', 9999))

# ส่งข้อมูล >> แปลงข้อมูลที่จะส่งเป็น unicode
client.send("Hello Server!".encode('utf-8'))
client.send("  I'm TCP!".encode('utf-8'))
# รับข้อมูล 1024 bytes (Buffer size) >> ถอดรหัส unicode
print(client.recv(1024).decode('utf-8'))

client.send("OK, Bye!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))