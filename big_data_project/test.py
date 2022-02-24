import socket, threading

def binder(client_socket, addr):

    print('connected by :', addr)
    try:
        while 1:
            data = client_socket.recv(4)
            lenth = int.from_bytes(data, 'little')
            data = client_socket.recv(lenth)
            msg = data.decode()
            print(msg)

            msg = 'echo :' + msg
            data = msg.encode()
            lenth = len(data)
            client_socket.sendall(lenth.to_bytes(4, byteorder='little'))
            client_socket.sendall(data)
    except:
        print('except :', addr)
    finally:
        client_socket.close()

def main():
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sever_socket.bind(('',9999))
    sever_socket.listen()

    try:
        while 1:
            client_socket, addr = sever_socket.accept()
            th = threading.Thread(target=binder, args=(client_socket, addr))
            th.start()

    except:
        print('sever')
    finally:
        sever_socket.close()

if __name__ == '__main__':
    main()
