import socket

#local host
IP_ADDRESS = '127.0.0.1'  #Ip address
PORT = 49152              #port number

#IPv4形式でソケット作成
socket_server = socket.socket(socket.AF_INET)

#IPアドレスとポート番号のバインド
socket_server.bind((IP_ADDRESS, PORT))

#サーバの有効化
socket_server.listen()

datasize_byte = 1024

#接続・受信
while True:
    socket_client, address = socket_server.accept()

    data = socket_client.recv(datasize_byte)

    print(data.decode('utf-8'))

    socket_client.close()


