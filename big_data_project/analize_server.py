import socket
import threading
import argparse
from multiprocessing import Process, Queue
import configparser

import mariadb


def arg_reader():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', type=str, default='db_conf.txt')
    return parser.parse_args().conf


def conf_reader(conf_file):
    result = dict()
    conf = configparser.ConfigParser()
    conf.read(conf_file)
    for i in conf.sections():
        for j in conf.options(i):
            result[j] = conf[i][j]
    return result


def binder(client_socket, addr, q):
    print('connected by :', addr)
    while 1:
        try:
            data = client_socket.recv(4)
            lenth = int.from_bytes(data, 'little')
            data = client_socket.recv(lenth)
            msg = data.decode()
            q.put(msg)

            msg = 'echo :' + msg
            data = msg.encode()
            lenth = len(data)
            client_socket.sendall(lenth.to_bytes(4, byteorder='little'))
            client_socket.sendall(data)
        except:
            client_socket.close()
            print('except :', addr)
            break

def sql_input(data):
    print(data)
    return 'SHOW TABLES'


def save_q(q):
    counter = 1
    while 1:
        try:
            data = q.get()
            sql = sql_input(data)
            db = mariadb.MariaDB(conf_reader(arg_reader()))
            db.conn_db()
            db.input_data(sql)
            #print('saved', data, counter)
            counter += 1
        except:
            print('save end')
            break


def cacul():
    pass


def socket_recv_server(q):
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sever_socket.bind(('', 9999))
    sever_socket.listen()
    while 1:
        try:
            client_socket, addr = sever_socket.accept()
            th = threading.Thread(target=binder, args=(client_socket, addr, q))
            th.start()
        except:
            print('socket_server end')
            break
    sever_socket.close()

def main():
    q = Queue()
    pr = Process(target=socket_recv_server, args=(q,))
    pv = Process(target=save_q, args=(q,))

    pv.start()
    pr.start()


if __name__ == '__main__':
    main()
