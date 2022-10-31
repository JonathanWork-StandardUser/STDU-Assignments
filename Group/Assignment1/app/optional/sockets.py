import socket

HOST = "192.168.254.77"
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall("Hello, Allen".encode())
    data = s.recv(10240)

print(f"Recieved {data!r}")