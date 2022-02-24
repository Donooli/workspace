import socket, threading

HOST = '127.0.0.1'
PORT = 9999

HW_cache = {
                0:{
                    0:{},   #CPU_1s_val
                    1:{},   #CPU_1m_avg
                    2:{}    #CPU_5m_peak
                },
                1:{
                    0:{},   #RAM_5s_val
                    1:{},   #RAM_5m_avg
                },
                2:{
                    0:{},   #DISK_1m_val
                    1:{},   #DISK_30m_avg
                    2:{}    #CPU_peak_DISK
                }
            }
global asd
asd = 0

def trans(data):
    a = int(data[0])
    b = int(data[1])
    c = float(data[2])
    return [a,b,c]

def binder(client_socket, addr):
    global asd
    print(f"Connected by : {addr[0]}:{addr[1]}")
    try:
        while 1:
            data = client_socket.recv(4)
            length = int.from_bytes(data, "little")
            data = client_socket.recv(length)
            msg = data.decode()
            msg_list = msg.split(' ')
            msg_list = trans(msg_list)
            HW_cache[msg_list[0]][0][msg_list[1]] = msg_list[2]
            if asd == 0:
                asd = msg_list[1]

            if msg_list[1] == asd:
                del HW_cache[msg_list[0]][0][msg_list[1]]

            print(f'Received {msg}')

            if (msg_list[0] == 0) and (msg_list[1] % 100 == asd % 100):
                asd_sum = 0.0
                asd_len = 0.0
                for i,j in HW_cache[0][0].items():
                    if (i > (msg_list[1] - 100)) or (i <= (msg_list[1])):
                        asd_sum += j
                        asd_len += 1
                print(asd_sum)
                print(asd_len)
                HW_cache[msg_list[0]][1][msg_list[1]] = asd_sum/asd_len
                if (msg_list[0] == 0) and (msg_list[1] % 500 == asd % 500):
                    max_key = 0
                    max_value = 0.0
                    for i,j in HW_cache[0][1].items():
                        if (i > (msg_list[1] - 500)) or (i <= (msg_list[1])):
                            if max_value <= j:
                                max_key = i
                                max_value = j
                    HW_cache[msg_list[0]][2][max_key] = max_value
                    for i,j in HW_cache[2][0].items():
                        if i == max_key:
                            HW_cache[msg_list[2]][2][i] = j



            if (msg_list[0] == 1) and (msg_list[1] % 500 == asd % 500):
                asd_sum = 0.0
                asd_len = 0.0
                for i,j in HW_cache[1][0].items():
                    if (i > (msg_list[1] - 500)) or (i <= (msg_list[1])):
                        asd_sum += j
                        asd_len += 1
                print(asd_sum)
                print(asd_len)
                HW_cache[msg_list[0]][1][msg_list[1]] = asd_sum/asd_len



            if (msg_list[0] == 2) and ((msg_list[1] % 10000 == asd % 10000) or (msg_list[1] % 10000  == asd % 10000 - 3000) or (msg_list[1] % 10000  == asd % 10000 + 3000)):
                asd_sum = 0.0
                asd_len = 0.0
                for i,j in HW_cache[2][0].items():
                    if (i > (msg_list[1] - 3000 ) if msg_list[1] % 10000 > 3000 else (msg_list[1] - 7000 )) or (i <= (msg_list[1])):
                        asd_sum += j
                        asd_len += 1
                print(asd_sum)
                print(asd_len)
                HW_cache[msg_list[0]][1][msg_list[1]] = asd_sum/asd_len


            msg = "echo : " + msg
            data = msg.encode()
            length = len(data)
            client_socket.sendall(length.to_bytes(4, byteorder="little"))
            client_socket.sendall(data)
    except:
        print(f"Disconnected by : {addr[0]}:{addr[1]}")
    finally:
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST,PORT))
server_socket.listen()

try:
    while True:
        client_socket, addr = server_socket.accept()
        th = threading.Thread(target=binder, args=(client_socket, addr))
        th.start()
except:
    print("server closed")
finally:
    print(HW_cache)
    server_socket.close()