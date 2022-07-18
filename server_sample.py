import socket
from client_sample import BUFFER_SIZE_BYTE

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
          data = socket_client.recv(BUFFER_SIZE_BYTE)
          print(data.decode('utf-8'))
          socket_client.close()


