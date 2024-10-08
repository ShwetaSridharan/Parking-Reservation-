# Parking Reservation System
A Client-Server based Parking Reservation System for the Education Car park building at the University of Alberta done as part of MINT 706.


## HOW TO RUN THE PROGRAM:
1. Download and Unzip the project file and you will find three files- edmts.client, edmts.server and parking.pickle. Open two command prompts- one for the server and one for the client.
2. In the first command prompt, type edmts.server and press enter. The server will display the server ip and port it is currently running on.
3. In the second command prompt, type 'edmts.client.py <ip address> <port> ask/reserve'
example: edmts.client.py 192.168.0.23 1234 reserve
This will display the reply from the server for the requested query.
4.With every reservation, 1 is decremented from the number of parking spaces available and the value is modified and stored in the parking.pickle file. After the value reaches 0, the server replies with a 'failed reservation'.
