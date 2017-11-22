#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

# UDP socket Client

import socket

so_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    so_cli.sendto(data, ('127.0.0.1', 8888))
    # 接收数据:
    print(so_cli.recv(1024).decode('utf-8'))

so_cli.close()