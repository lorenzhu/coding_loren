#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

# TCP socket Client

import socket
so_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

so_cli.connect(('127.0.0.1', 9999)) # 建立连接

print(so_cli.recv(1024).decode('utf-8'))	# 接收并打印服务器端的欢迎消息“Welcome!”
for data in [b'Micheal', b'Tracy', b'Sarah']:
	so_cli.send(data) # 发送数据
	print(so_cli.recv(1024).decode('utf-8'))# 打印返回的数据

# 手动输入并发送一些文字 # 不输入，直接回车有bug
hello = bytes(input('Say something: '), encoding="utf-8") # str to bytes
so_cli.send(hello)
print(so_cli.recv(1024).decode('utf-8'))

so_cli.send(b'exit')
so_cli.close()