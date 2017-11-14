#!/usr/bin/env python3
# client.py

# 导入 socket, sys 模块
import socket, sys

# 创建 socket 对象
clientso =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
print('host: ', host)

# 设置端口号
port = 6666

# 连接服务，指定主机和端口
clientso.connect((host, port))
#clientso.connect(('127.0.0.1', port))


# 接收小于 1024kb 的数据
message = clientso.recv(1024)

clientso.close()

print(message.decode('utf-8'))
