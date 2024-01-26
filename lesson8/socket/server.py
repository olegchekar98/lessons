import socket
from time import sleep


def main():
    host = socket.gethostname()
    port = 5011

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(10)

    conn, addr = server_socket.accept()

    print('socket from',addr)

    while True:
        data = conn.recv(1024)
        print('data',data)
        if data.decode() == 'pass_me':
            print(data)
            conn.send('you passed security check'.encode())

            if not data:
                break
        else: break

    conn.close()


if __name__ == '__main__':
    main()




