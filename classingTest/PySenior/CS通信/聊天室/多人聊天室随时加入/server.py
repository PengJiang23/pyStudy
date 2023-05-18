import select
from socket import *
import sys

# 随时加入功能bug


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 重定向，当服务器被ctrl+c终止，端口进入timewait状态不会直接关闭
    # 方便测试，重定向后，再次运行服务器不会提示地址被使用
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    # epoll对象
    epoll = select.epoll()
    # 开启监测
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    epoll.register(s.fileno(), select.EPOLLIN)
    client_dict = {}
    while True:
        events = epoll.poll(-1)  # 存储监测的文件句柄，变化返回
        for fd, event in events:
            if fd == s.fileno():
                cs_socket, clientAddr = s.accept()
                client_dict.setdefault(cs_socket.fileno(), cs_socket)
                epoll.register(cs_socket.fileno(), select.EPOLLIN)
                """
                当前字典中所有用户
                1、当前用户接收到数据，检查数据有效性
                2、转发给除了与该fd相同的所有其他用户           
                """
            elif fd == sys.stdin.fileno():
                try:
                    data = input()
                except EOFError:
                    print('eof error')
                    return
                str_data = ("服务器：" + data).encode('utf8')
                for fileno in client_dict:
                    client_dict[fileno].send(str_data)
            else:
                for fileno in client_dict:
                    if fd != fileno:  # 非当前用户
                        recv_data = client_dict[fd].recv(100)
                        if recv_data:
                            # 转发数据
                            print(recv_data.decode('utf8'))
                            client_dict[fileno].send(recv_data)
                        else:
                            print('客户端断开连接')  # 关闭监听、释放套接字
                            client_dict.pop(fd)
                            epoll.unregister(client_dict[fileno].fileno())
                            cs_socket.close()
                            continue  # 断开连接还是保持监听

    cs_socket.close()
    s.close()


if __name__ == '__main__':
    server()
