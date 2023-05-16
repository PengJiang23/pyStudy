import socket

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('192.168.31.218',2000)
    s.bind(addr)
