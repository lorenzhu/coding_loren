#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

# TCP socket Server

import socket
import time
import threading
so_ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口， 监听客户端连接
so_ser.bind(('127.0.0.1', 9999))

# 开始监听端口
so_ser.listen(5)  # 参数指定等待链接的最大数量
print('Waiting for connection...')

# 每个连接都必须创建新线程（或进程）来处理，
# 否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
		print(addr) # 为什么这里可以
	sock.close()
	print('Connection from %s:%s is closed.' % addr)

while True:  # 永久循环，接受来自客户端的连接
    sock, addr = so_ser.accept() # 接受一个新连接
	#print(addr) # 为什么这里就不可以！！！
    # 创建新线程来处理TCP连接:
    thread_ser = threading.Thread(target=tcplink, args=(sock, addr))
    thread_ser.start()
	

	
