import socket

#local host
IP_ADDRESS = '127.0.0.1'  #Ip address
PORT = 49152              #port number

#クライアント側のソケット作成
socket_client = socket.socket(socket.AF_INET)

#サーバへ接続
socket_client.connect((IP_ADDRESS, PORT))

transmission_data_byte = 'Hello World'

socket_client.send(transmission_data_byte.encode('utf-8'))