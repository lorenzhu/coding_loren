# 目标计算机的 【IP + 端口号】

# 导入socket库：
import socket

# 创建一个socket
myso = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET: IPv4协议, AF_INET6 : IPv6
# SOCK_STREAM指定使用面向流的TCP协议


# 建立连接：
myso.connect(('www.baidu.com', 80))  # 183.232.24.222 #sysu 121.46.26.52
#	IP地址可以用域名www.sina.com.cn自动转换到IP地址
#	80 Web, 25 SMTP, 21 FTP, >1024 任意使用


# 发送数据：
myso.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#  s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端


# 接收数据：
buffer = []
while True:
	# 每次最多接收1KB
	d = myso.recv(1024) #调用recv(max)方法，一次最多接收指定的字节数
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)


# 关闭连接：
myso.close()

# 分离HTTP头和网页
my_header, my_html = data.split(b'\r\n\r\n', 1)
print('---------------- header start -----------------\n')
print(my_header.decode('utf-8')) # 打印HTTP头
print('----------------- header end -----------------\n')

# 把接收的数据写入文件
with open('tcp_baidu.html', 'wb') as f:
	f.write(my_html)