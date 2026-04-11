import socket

server_socket = socket.socket()

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("localhost", 9999))
server_socket.listen(1)

print("server is waiting...")

client_socket, addr = server_socket.accept()
print("connected with:", addr)

client_socket.send(b"Hello from server")

client_socket.close()
server_socket