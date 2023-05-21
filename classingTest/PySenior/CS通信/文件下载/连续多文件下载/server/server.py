from socket import *
import select
import sys
import struct


s = socket(AF_INET, SOCK_STREAM)
addr = ('', 2001)
s.bind(addr)
s.listen(128)
filename = 'aaa'
c_socket, client_addr = s.accept()
filename_bytes = filename.encode('utf8')
filename_bytes_binary = struct.pack('I', len(filename_bytes))
c_socket.send(filename_bytes_binary+filename_bytes)

with open(filename, 'rb') as f:
    f_content = f.read()
    f_content_binary = struct.pack('I', len(f_content))
    c_socket.send(f_content_binary + f_content)
    f.close()
    c_socket.close()
    s.close()
