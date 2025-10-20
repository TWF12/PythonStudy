import socket

# 创建socket对象
server_socket = socket.socket()
# 绑定ip和端口
server_socket.bind(("localhost", 8888)) # 参数为元组,第一个元素为ip, 第二个元素为端口
# 监听客户端连接
server_socket.listen(1) # 参数表示最大连接数
# 等待客户端连接
conn, address = server_socket.accept() # coonn表示连接对象, address表示客户端地址
print("连接客户端成功,客户端地址为:", address)
while True:
    # 接受客户端发送的数据
    data = conn.recv(1024).decode("utf-8") # 参数表示最大接受数据量,返回值为字节数组,需要解码变成字符串
    print("收到客户端发送的数据为:", data)
    # 发送数据给客户端
    msg = input("请输入要发送给客户端的数据:").encode("utf-8") # 需要编码成字节数组
    if msg == b"exit":
        break
    conn.send(msg)
# 关闭连接
conn.close()
server_socket.close()

