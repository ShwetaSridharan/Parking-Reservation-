#Connecting to the Client
import socket, sys
import pickle
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip= socket.gethostbyname(socket.gethostname())
port= 1234
parking_spaces_available= 20
address=(server_ip, port)
s.bind(address)
s.listen(10)
print ("EDMTS is running on "+server_ip+ " listening on port " +str(port))

while True:
   #accepting messages(data) from the client in the receive buffer of the server and decoding it.
    clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established!")
    data= clientsocket.recv(2048)
    data_decoded= data.decode()

    #creating a pickle file to store the value of parking spaces available.
    pickle_out = open("parking.pickle", "wb")
    pickle.dump(parking_spaces_available, pickle_out)
    pickle_out.close()

    #defining the three types of decoded data the server will receive from the client.
    request1= "ask"
    request2= "reserve"
    request3= "exit"
   
    #When the Client asks the server for the number of parking spaces available currently:
    if data_decoded == request1:
    	clientsocket.send(bytes("Education Car Park has" + " " + str(parking_spaces_available) + " " + "spaces available.", "utf-8"))

    #client reserving a parking space.
    elif data_decoded== request2:
      #When there is no parking space available:
      if parking_spaces_available== 0:
         clientsocket.send(bytes("Failed Reservation","utf-8")) 
      else:
         #When there are parking spaces available upon request:
         #open the pickle file and update the value of parking_spaces_available.This value remains unchanged until the next reservation.
         pickle_in= open("parking.pickle", "rb")
         parking_spaces_available= pickle.load(pickle_in)
         #Decrement value by 1 each time a reservation is made by the client.
         parking_spaces_available-=1
         #Mentioned separately so as to make sure it uses the singular form of "space" for a single available parking space.
         if parking_spaces_available== 1:
            clientsocket.send(bytes("Space Reserved. Education Car Park now has" + " " + str(parking_spaces_available) + " " + "space available.", "utf-8"))
         #Result given to the client for values of parking_spaces_available other than 0 and 1.
         clientsocket.send(bytes("Space Reserved. Education Car Park now has" + " " + str(parking_spaces_available) + " " + "spaces available.", "utf-8"))

         #Close the opened pickle file with the modified value of parking_spaces_available.
         pickle_out.close()

    #If the Client sends any value other than the three request cases, the reply will be the following:
    else:
      clientsocket.send(bytes("Invalid Data. Please choose from either 'ask' or 'reserve'.", "utf-8"))

clientsocket.close()