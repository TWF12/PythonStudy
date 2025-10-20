import socket

# 创建socket对象
client_socket = socket.socket()
# 连接服务端
client_socket.connect(("localhost",8888))
while True:
    # 发送数据
    msg = input("请输入要发送给服务端的数据:")
    if msg == "exit":
        break
    client_socket.send(msg.encode("utf-8"))
    # 接收数据
    data = client_socket.recv(1024)
    print("收到服务端回复的数据:",data.decode("utf-8"))

# 关闭连接
client_socket.close()

