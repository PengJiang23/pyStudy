import select
from socket import *
import sys


def server():
    s = socket(AF_INET, SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    # epoll对象
    epoll = select.epoll()
    # 开启监测
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    epoll.register(s.fileno(), select.EPOLLIN)
    while True:
        events = epoll.poll(-1)  # 存储监测的文件句柄，变化返回
        for fd, event in events:
            if fd == s.fileno():       # 有无用户加入
                cs_socket, client_addr = s.accept()
                epoll.register(cs_socket.fileno(), select.EPOLLIN)
            if fd == cs_socket.fileno():
                recv_data = cs_socket.recv(100)
                if recv_data:
                    print(recv_data.decode('utf8'))
                else:
                    print('客户端断开连接')            # 关闭监听、释放套接字
                    epoll.unregister(cs_socket.fileno())
                    cs_socket.close()
                    break       # 断开连接还是保持监听
            elif fd == sys.stdin.fileno():
                try:
                    data = input()
                except EOFError:
                    print('eof error')
                    return
                cs_socket.send(data.encode('utf8'))
    cs_socket.close()
    s.close()


if __name__ == '__main__':
    server()
