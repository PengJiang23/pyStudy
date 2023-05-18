import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_addr = ('192.168.31.218', 3000)
server.bind(recv_addr)
recv_data, client_addr = server.recvfrom(299)
print(recv_data.decode('utf8'))
print(client_addr)
server.sendto(b'aaa', client_addr)
server.close()
