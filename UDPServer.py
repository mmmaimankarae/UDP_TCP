import socket

 # Create Socket Server #
# 2 parameters (type_of_socket, protocol) [AF_INET = IPv4, connection (Client-Server & Send-Receive)]
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket >> สร้าง(ผูก)IP Address ของ Server
server.bind(('192.168.1.115', 9999))

while True:
    # ฟังข้อมูลที่จะส่งมา >> ไม่ได้ฟังconnection ที่ติดต่อเข้ามา และไม่ได้อนุญาตให้ส่งข้อมูล แต่จะส่งก็ส่งมาเลยจ้า
        # buffer size ถ้าไม่มากพอข้อมูลอาจจะตกหล่น
    # recvform funtion return >> ค่า(ข้อมูล)ที่ส่งมา, IP Address
    message, address = server.recvfrom(1024)
    print(message.decode('utf-8'))
    
    # ส่งข้อมูลกลับ
    server.sendto("Hello UDP!".encode('utf-8'), address)