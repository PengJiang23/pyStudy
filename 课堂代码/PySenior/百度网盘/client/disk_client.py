from socket import *
import struct
import os

FILE_PROTOCAL_SIZE = 4


class Client:
    def __init__(self, ip, port):
        self.client: socket = None
        self.ip = ip
        self.port = port

    def tcp_init(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.ip, self.port))

    def send_command(self):
        """
        可以改进，使用dict，k-v -> command-函数名
        :return:
        """
        while True:
            command = input("输入命令")
            self.transmission_send_handle(command.encode('utf8'))
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd()
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm(command)
            elif command[:4] == 'gets':
                self.do_gets(command)
            elif command[:4] == 'puts':
                self.do_puts(command)
            elif command[:4] == 'exit':
                exit(0)
            else:
                print('wrong command')

    def transmission_send_handle(self, send_bytes):
        recv_head = struct.pack('I', len(send_bytes))
        self.client.send(recv_head + send_bytes)

    def transmission_recv_handle(self):
        recv_head = self.client.recv(FILE_PROTOCAL_SIZE)
        train_content = struct.unpack('I', recv_head)
        return self.client.recv(train_content[0])

    def do_ls(self):
        print(self.transmission_recv_handle().decode('utf8'))

    def do_cd(self):
        print(self.transmission_recv_handle().decode('utf8'))

    def do_pwd(self):
        print(self.transmission_recv_handle().decode('utf8'))

    def do_rm(self, command):
        pass

    def do_gets(self, command):
        """
        接收文件
        :param command:
        :return:
        """
        filename = command.split()[1]
        file_content_size = self.client.recv(4)
        filesize = struct.unpack('I', file_content_size)
        total = 0
        with open("下载" + filename, 'wb')as f:
            while total <= filesize[0]:
                data = self.client.recv(1000)
                f.write(data)
                total += len(data)
                print('\r %5.2f%s' % (total / filesize[0] * 100, '%'), end='')
            print('\r100.00%')
        f.close()

    def do_puts(self, command):
        filename = command.split()[1]
        file_size = os.stat(filename).st_size
        self.client.send(struct.pack('I', file_size))
        with open(filename, 'rb') as f:
            while True:
                file_content = f.read(1000)
                if file_content:
                    self.client.send(file_content)
                else:
                    break
            f.close()


if __name__ == '__main__':
    client = Client('127.0.0.1', 4001)
    client.tcp_init()
    client.send_command()
