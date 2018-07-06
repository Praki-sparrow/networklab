# networklab
import socket
UDP_IP_ADDRESS="10.1.24.131"
UDP_PORT_NO=6789
serversock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))
print("server is waiting")
while True:
 data,addr=serversock.recvfrom(1024)
 print("message:",data)
