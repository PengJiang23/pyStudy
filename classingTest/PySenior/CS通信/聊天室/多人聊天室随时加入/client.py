import select
import socket
import sys


def client():
    if len(sys.argv) == 1:
        return
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clinentAddr = (sys.argv[1], 2000)
    c.connect(clinentAddr)
    epoll = select.epoll()
    epoll.register(c.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    name = input("输入名字")
    while True:
        events = epoll.poll(-1)
        for fd, event in events:
            if fd == c.fileno():
                data = c.recv(100)
                if data:
                    print(data.decode('utf8'))
                else:
                    print("服务器断开了")
                    return
            elif fd == sys.stdin.fileno():
                data = input()
                str_data = (name + '：' + data).encode('utf8')
                c.send(str_data)
    c.close()


if __name__ == '__main__':
    client()
