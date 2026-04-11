import socket

client_socket = socket.socket()

client_socket.connect(("localhost", 9999))

data = client_socket.recv(1024)

print("message from server:", data.decode())

client_socket.close()