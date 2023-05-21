import socket
import sys


def get_fileContent(filename):
    try:
        with open(filename, 'rb') as f:
            content = f.read()
        return content
    except:
        print(f"{filename}没有这个文件")


def main():
    if len(sys.argv) != 2:
        return
    else:
        port = int(sys.argv[1])

    # 建立tcp连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', port)
    s.bind(addr)
    s.listen(128)

    while True:
        new_socket, client_addr = s.accept()
        rdata = new_socket.recv(100)
        file_name = rdata.decode('utf8')
        file_content = get_fileContent(file_name)

        if file_content:
            new_socket.send(file_content)
        new_socket.close()
        s.close()


if __name__ == '__main__':
    main()
