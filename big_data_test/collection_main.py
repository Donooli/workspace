import time
import multiprocessing as mp
from multiprocessing import Process, Queue, Pipe
import psutil
import argparse
import configparser

def arg_reader():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', type = str , default='conf.txt')
    return vars(parser.parse_args()).values()

def conf_reader(conf_file):
    result = dict()
    conf = configparser.ConfigParser()
    conf.read(conf_file)
    section = conf.sections()
    for i in section:
        result[i] = conf[i]['interval']
    return result

def make_process(q1,q2,**data):
    for key,val in data.items():
        val = int(val)
        if key == 'cpu':
            print('make cpu process sucess')
            cpu_pro = Process(target=cpu_collector, args=(q1,q2,val))
            cpu_pro.start()

        elif key == 'mem':
            print('make mem process sucess')
            mem_pro = Process(target=mem_collector, args=(q1,q2,val))
            mem_pro.start()

        elif key == 'disk':
            print('make disk process sucess')
            disk_pro = Process(target=disk_collector, args=(q1,q2,val,'c://'))
            disk_pro.start()

def collection_run():
    pass

def cpu_collector(q1,q2,interval):
    while 1:
        if q1.get()%interval == 0:
            print(interval)
            #q2.put(psutil.cpu_percent(None))

def mem_collector(q1,q2,interval):
    while 1:
        if q1.get()%interval == 0:
            print(interval)
            #q2.put(psutil.virtual_memory().percent)

def disk_collector(q1,q2,interval,disk_name):
    while 1:
        if q1.get()%interval == 0:
            print(interval)
            #q2.put(psutil.disk_usage(disk_name).percent)

def time_tick(q1):
    counter = 0
    while 1:
        time.sleep(1 - time.time() % 1)
        counter += 1
        try:

            q1.put(counter)
            print(time.time())
            if counter == 60:
                counter = 0
        except:
            break

def main():
    #data = conf_reader(arg_reader())
    #print(data)
    q1 = Queue()
    q2 = Queue()
    q3 = Queue()
    #q2 = Queue()
    #make_process(q1,q2,**data)
    #print('start')
    #time_tick(q1)
    timer_1 = Process(target=time_tick,args=(q1,))
    timer_2 = Process(target=time_tick,args=(q2,))
    timer_3 = Process(target=time_tick,args=(q3,))

    timer_1.start()
    timer_2.start()
    timer_3.start()



if __name__ == '__main__':
    main()
