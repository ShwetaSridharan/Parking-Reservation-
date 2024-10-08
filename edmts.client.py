#Connecting to the server and sending command line arguments
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) == 4:
	ip= sys.argv[1]
	port= int(sys.argv[2])
	command_request= sys.argv[3]
address_client= (ip, port)
s.connect(address_client)

while True:
	s.send(command_request.encode())	
	#specifying the receive buffer and decoding the reply from the server
	msg= s.recv(1024)
	print (msg.decode("utf-8"))
	#Breaking and closing the connection to the server after every request and reply pair.
	break
s.close()



	



