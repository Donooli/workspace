import socket

class CollectionSever:
    def __init__(self,HOST,PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST,self.PORT))

    def sever_run(self,data):
        try:
            msg = data
            data = msg.encode()
            length = len(data)
            self.client_socket.sendall(length.to_bytes(4, byteorder="little"))
            self.client_socket.sendall(data)

            data = self.client_socket.recv(4)
            length = int.from_bytes(data, "little")
            data = self.client_socket.recv(length)
            msg = data.decode()
            print('Received from : ', msg)

        finally:
            self.client_socket.close()