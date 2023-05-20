import socket

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.31.218',2000)
    s.bind(addr)
    s.listen(128) # 监听数目
    client_socket, client_addr = s.accept()
    data = client_socket.recv(100)
    print(data.decode('utf8'))
    client_socket.send('来自服务器的数据'.encode('utf8'))
    client_socket.close()
    s.close()

if __name__ == '__main__':
    tcp_server()