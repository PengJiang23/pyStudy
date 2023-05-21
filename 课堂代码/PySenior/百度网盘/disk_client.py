from socket import *
import struct

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
        pass

    def do_puts(self, command):
        pass


if __name__ == '__main__':
    client = Client('127.0.0.1', 4000)
    client.tcp_init()
    client.send_command()
