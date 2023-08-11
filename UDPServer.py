import socket

# Create Socket Server
# 2 parameters (type_of_socket, protocol)
# AF_INET = IPv4, connection (Client-Server & Send-Receive)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind socket >> สร้างIP Address ของ Server
server.bind(('127.0.0.1', 9999))

# ฟังข้อมูลที่จะส่งมา >> ไม่ได่อนุญาตให้ส่ง จะส่ก็ส่งมาเลยจ้า
# buffer size ถ้าไม่มากพอข้อมูลอาจจะตกหล่น
# recvform funtion return >> ค่าที่ส่งมา, IP Address
message, address = server.recvfrom(1024)
print(message.decode('utf-8'))

# ส่งข้อมูลกลับ
server.sendto("Hello Client!".encode('utf-8'), address)