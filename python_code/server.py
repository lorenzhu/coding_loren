#!/usr/bin/python3
# server.py

# 导入 socket, sys 模块
import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
localhost = socket.gethostname()
print('本地主机名：', localhost)  # Loren

port = 6666

# 绑定端口
serversocket.bind((localhost, port))
#serversocket.bind(('127.0.0.1', port))

#设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print('连接地址： %s' % str(addr))

    msg = '欢迎访问 SYSU-Library Seats Distribution System!\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
