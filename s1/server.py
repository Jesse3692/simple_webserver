# -*- encoding: utf-8 -*-
'''
@File    : server.py
@Time    : 2020/04/10 23:59:07
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : None
'''


import socket

listener = socket.socket()
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(('0.0.0.0', 8080))
listener.listen(1)
print('Serving HTTP on 0.0.0.0 port 8080 ...')

while True:
    conn, addr = \
        listener.accept()
    print(f'Server received connection from {addr}')
    request = conn.recv(1024)
    print(f'request we received: {request}')
    response = b'HTTP/1.1 200 OK\r\n\r\nHello, World!\r\n'
    conn.sendall(response)
    conn.close()
