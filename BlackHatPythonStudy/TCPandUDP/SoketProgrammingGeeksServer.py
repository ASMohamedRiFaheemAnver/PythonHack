
#What is socket programming in python
#From https://www.geeksforgeeks.org/socket-programming-python/

import socket
import sys

#Here we can find the definition of TCP and UDP and difference between them
#https://enterprise.netscout.com/edge/tech-tips/difference-between-tcp-and-udp


#You can see the difference between AF_INET, PF_INET here
#https://stackoverflow.com/questions/6729366/what-is-the-difference-between-af-inet-and-pf-inet-in-socket-programming

#Unhandled Exception
"""
#Creating a instance
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Finding Ip in terminal (PING www.google.com) or

ip = socket.gethostbyname("www.google.com")
print(ip)
"""

#Handling exception
"""
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with %s" %(err))

#Default port for the socket
port = 80

try:
    hostIp = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("There is an error resolving the host")
    sys.exit()

#Connecting to the server
#Host and Port must be tuple
#https://stackoverflow.com/questions/19143091/typeerror-connect-takes-exactly-one-argument
s.connect((hostIp, port))
print("The socket has successfully connected to google on port : %s"% hostIp)
"""

#Server Program


#Creating socket object
s = socket.socket()
print("Socket successfully created")

port = 12345

#Make sever to listen to requests
s.bind(('', port))
print("Socket binded to %s"% (port))

#Put the socket into listening mode
s.listen(5)
print("Socket is listening")

#A forever loop
while(True):
    #Establish connection with client
    c, addr = s.accept()
    print("Got connction from", (addr))

    #Sending a thank you message to the client
    #Got error with python 3
    #https://stackoverflow.com/questions/33003498/typeerror-a-bytes-like-object-is-required-not-str
    c.send("Thank you for connecting".encode())
    #Close the connection with the client
    c.close() 