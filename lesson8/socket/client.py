import socket
import datetime


def client():
    host = socket.gethostname()
    port = 5011

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = 'pass_me'

    client_socket.send(message.encode('utf-8'))

    while True:
        data = client_socket.recv(1024)
        print(data)

        if not data:
            break

    client_socket.close()


if __name__ == '__main__':
    client()