import socket

targetHost = "www.google.com"
targerPort = 80

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((targetHost, targerPort))

#send some data
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data.encode("utf-8"))

#receive some data
response = client.recv(4096)

#printing the response
print(response)