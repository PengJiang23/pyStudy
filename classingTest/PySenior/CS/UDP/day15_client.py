# UDP通信
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr = ('192.168.31.218', 3000)
client.sendto('你好'.encode('utf8'),dest_addr)
data,_=client.recvfrom(200)
print(data.decode('utf8'))
client.close()
