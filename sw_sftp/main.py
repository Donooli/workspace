import paramiko
import argparse
import time
from multiprocessing import Process

PORT1 = 2201

def arg_reader():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', type = str)
    parser.add_argument('--host', type = str)
    parser.add_argument('--pwd', type = str)
    return parser.parse_args()

def conn_sftp(user, host, pwd, port):
    transport = paramiko.transport.Transport((host, port))
    print('connect success')
    transport.connect(username=user, password=pwd)
    print('user info input')
    sftp = paramiko.SFTPClient.from_transport(transport)
    print('--------------------------------------------')
    return sftp

def find_files(data,camnum):
    local_path = '%local_path'
    root_path = f'surveillance/testatetri-{camnum}'
    root = data.listdir(root_path)
    for i in root[:4]:
        if '20' in i:
            if (int(i[:-2])>=20220201) or (int(i[:-2]) < int(time.strftime('%y%m%d'))):
                lsdata = data.listdir(f'{root_path}/{i}')
                for j in lsdata:
                    if '.mp4' in j:
                        print(j)

def main():
    user = arg_reader().user
    host = arg_reader().host
    pwd = arg_reader().pwd
    port = PORT1
    data = conn_sftp(user,host,pwd,port)
    find_files(data,2)


if __name__ == '__main__':
    main()
