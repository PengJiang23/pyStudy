import socket
import sys


def client():
    # 客户端建立tcp连接
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serve_addr = ('192.168.31.218', 3000)
    client_socket.connect(serve_addr)
    filename = input("输入下载的文件名")
    client_socket.send(filename.encode('utf8'))
    data = client_socket.recv(200)
    if data:
        with open("复制的" + filename, "wb") as f:
            f.write(data)
    client_socket.close()


if __name__ == '__main__':
    client()
