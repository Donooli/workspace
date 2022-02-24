import collection_sever as cs
import threading
from threading import Timer
import multiprocessing as mp
from multiprocessing import Process
import cpu_info,ram_info,disk_info
import time


def collection_sever_run(data):
    con = cs.CollectionSever('127.0.0.1', 9999)
    con.sever_run(data)

def cpu_t():
    start_time = time.time()
    collection_sever_run(f'0 {time.strftime("%Y%m%d%I%M%S", time.localtime())} {cpu_info.cpu_use_percent(None)}')
    end_time = time.time()
    threading.Timer(1-(end_time-start_time)%1, cpu_t).start()

def ram_t():
    start_time = time.time()
    collection_sever_run(f'1 {time.strftime("%Y%m%d%I%M%S",time.localtime())} {ram_info.ram_use_percent()}')
    end_time = time.time()
    threading.Timer(5-(end_time-start_time)%1, ram_t).start()

def disk_t():
    start_time = time.time()
    collection_sever_run(f'2 {time.strftime("%Y%m%d%I%M%S",time.localtime())} {disk_info.disk_use_percent()}')
    end_time = time.time()
    threading.Timer(60-(end_time-start_time)%1, disk_t).start()

if __name__ == '__main__':
    print('start_collect')
    '''pt =mp.Process(target=test)
    pt.start()
    pt.join()'''
    try:
        p1 = mp.Process(target=cpu_t)
        p2 = mp.Process(target=ram_t)
        p3 = mp.Process(target=disk_t)

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()
    except KeyboardInterrupt:
        print('stop_collection')