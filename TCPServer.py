import socket

# Create Socket Server
# 2 parameters (type_of_socket, protocol)
# AF_INET = IPv4, connection (Client-Server & Send-Receive)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket >> สร้างIP Address ของ Server
server.bind(('127.0.0.1', 9999))

# ฟังข้อมูลที่จะส่งมา
server.listen()

while True:
    # accept function return >> socket ที่ใช้ติดต่อกับClient, address ของ Client
    client, address = server.accept()
    print(f"Connected to {address}")
    # รับข้อมูล 1024 bytes
    print(client.recv(1024).decode('utf-8'))
    # ส่งข้อมูลกลับ
    client.send("Hello Client!".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.send("Bye!".encode('utf-8'))
    # ปิดClient
    client.close()