import socket
import pickle

#local host
IP_ADDRESS = '127.0.0.1'  #Ip address
PORT = 8080              #port number
BUFFER_SIZE_BYTE = 2048   #buffer size[byte]

#IPv4形式でソケット作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     s.bind((IP_ADDRESS, PORT))
     s.listen(10)
     while True:
        socket_client, client_address = s.accept()
        print('接続したクライアント情報:', str(client_address))
        data = socket_client.recv(BUFFER_SIZE_BYTE)
        if not data:
           break
        data = pickle.loads(data)
        print(data)
        socket_client.close()


