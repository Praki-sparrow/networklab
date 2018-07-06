import socket
UDP_IP_ADDRESS="10.1.24.131"
UDP_PORT_NO=6789
message=("good afternoon")
byteToSend=str.encode(message)
clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsock.sendto(byteToSend,(UDP_IP_ADDRESS,UDP_PORT_NO))
