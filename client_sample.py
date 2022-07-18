import socket
import pickle

#local host
IP_ADDRESS = '127.0.0.1'  #Ip address
PORT = 8080             #port number
BUFFER_SIZE_BYTE = 2048   #buffer size [byte]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #サーバへ接続
    s.connect((IP_ADDRESS, PORT))
    transmission_data_byte = b'Hello World'
    s.send(transmission_data_byte.encode('utf-8'))