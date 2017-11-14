#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

# UDP socket Server
# 不需要建立连接，可靠性差，但真的比TCP快很多

import socket

so_ser = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# SOCK_DGRAM指定了这个Socket的类型是UDP

# 绑定端口
so_ser.bind(('127.0.0.1', 8888))

print('Bind UDP on 8888...')
while True:
    # 接收数据:
    data, addr = so_ser.recvfrom(1024) # 返回数据和客户端的地址与端口
    print('Received from %s:%s  Message:' % addr, data.decode('utf-8'))
   #print('Received from %s:%s.' % addr)
    so_ser.sendto(b'Hello, %s!' % data, addr)

so_ser.close()

