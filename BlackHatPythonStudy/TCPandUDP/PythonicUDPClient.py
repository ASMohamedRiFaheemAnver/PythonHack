# From https://pythontic.com/modules/socket/udp-client-server-example

import socket

msgFromClent = "Hello UDP Server"
byteToSend = str.encode(msgFromClent)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send msg to server
UDPClientSocket.sendto(byteToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

print(msgFromClent)
UDPClientSocket.close()