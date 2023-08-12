import socket

    # Create Socket Server #
# 2 parameters (type_of_socket, protocol) [AF_INET = IPv4, connection (Client-Server & Send-Receive)]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket >> สร้าง(ผูก)IP Address ของ Server
server.bind(('192.168.1.115', 9999))

# method ฟังconnection ที่ขอติต่อเข้ามา
server.listen()

while True:
    # accept function return >> socket ที่Clientใช้, address ของ Client
    client, address = server.accept()
    # แสดงข้อมูล IPaddress และ Port ของDestination
    print(f"Connected to {address}")
    
    # รับข้อมูล 1024 bytes (Buffer size) >> ถอดรหัส unicode
    print(client.recv(1024).decode('utf-8'))
    
    # ส่งข้อมูลกลับ >> แปลงข้อมูลที่จะส่งเป็น unicode
    client.send("Hello!, TCP Cliect.".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    
    client.send("Bye!".encode('utf-8'))
    
    # ปิดconnection ที่เชื่อมกับClient: จบการทำงานจากการเชื่อมต่อClient-Server
    client.close()