import socket
import pickle

#local host
# IP_ADDRESS = '127.0.0.1'  #Ip address
IP_ADDRESS = '192.168.2.103' #My Raspberry Pi IP address
#PORT = 8080              #port number
PORT = 24000              #DYNAMIC AND/OR PRIVATE PORTS
BUFFER_SIZE_BYTE = 2048   #buffer size[byte]

new_list = []

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
        new_list.append(data[2])
        print(data)
        print(new_list)
        socket_client.close()


