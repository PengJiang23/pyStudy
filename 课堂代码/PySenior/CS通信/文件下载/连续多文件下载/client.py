import struct
from socket import *
import select

client = socket(AF_INET, SOCK_STREAM)
client_addr = ('192.168.31.218', 2001)
client.connect(client_addr)
filename_binary = client.recv(4)
content_len = struct.unpack('I', filename_binary)
filename = client.recv(content_len[0])
print(filename.decode('utf8'))
with open(filename.decode('utf8'), 'wb') as f:
    head = client.recv(4)
    content_len = struct.unpack('I', head)
    file_content = client.recv(content_len[0])
    f.write(file_content)
    f.close()
    client.close()
