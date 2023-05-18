import socket


def tcp_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.31.218', 2000)
    c.connect(addr)
    c.send('客户端发送的数据'.encode('utf-8'))
    data = c.recv(100)
    print(data.decode('utf8'))
    c.close()


if __name__ == '__main__':
    tcp_client()
