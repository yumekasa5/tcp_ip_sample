from http import client
import socket
import pickle

#local host
IP_ADDRESS = '127.0.0.1'  #Ip address
PORT = 8080             #port number
BUFFER_SIZE_BYTE = 2048   #buffer size [byte]

data_list = [i for i in range(10)]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))
transmission_data_byte = pickle.dumps(data_list)
client_socket.send(transmission_data_byte)
client_socket.close()