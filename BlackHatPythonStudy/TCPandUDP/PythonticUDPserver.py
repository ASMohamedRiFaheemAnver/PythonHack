# From https://pythontic.com/modules/socket/udp-client-server-example

import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Initializing encoding to byte
msgFromServer = "Hello UDP Client"
byteToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to Address and IP
UDPServerSocket.bind((localIP, localPort))
print("UDP Server up and listening")

# Listen for incoming datagrams

while(True):
    byteAddressPair = UDPServerSocket.recvfrom(bufferSize)
    print(byteAddressPair)
    # Sending a replay to client
    UDPServerSocket.sendto(byteToSend, byteAddressPair[1])