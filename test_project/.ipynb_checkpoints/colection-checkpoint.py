import time
import psutil
import multiprocessing as mp
from multiprocessing import Process
import threading
from threading import Timer

def cpu_percent():
    return psutil.cpu_percent(interval=1)          
    
def ram_percent():
    return psutil.virtual_memory().percent
    
def disk_percent():
    return psutil.disk_usage('c://').percent

def hw_print(func):
    print(func)

def timer(func,interval):
    hw_print(func)
    t = threading.Timer(interval,timer)
    t.start()
    
    
def main():
    print('-------------------collecting start-------------------')
    start_time = int(time.time())
    end_time = start_time
    time_gap = 0
    p1 = mp.Process(target = timer(hw_print(cpu_percent()),1))
    p2 = mp.Process(target = timer(hw_print(ram_percent()),5))
    p3 = mp.Process(target = timer(hw_print(disk_percent()),60))
    
    p1.daemon
    p2.daemon
    p3.daemon
    
    p1.start()
    p2.start()
    p3.start()
    
        #try:
#            now_time = int(time.time())
#            if end_time != now_time:
#                end_time = now_time
#                time_gap = end_time-start_time
#                if time_gap % 1 == 0:
#                    p1.start()
#                if time_gap % 5 == 0:
#                    p2.start()
#                if time_gap % 60 == 0:
#                    p3.start()
#                print('------------------------------------------------------')
            
#        except KeyboardInterrupt as e:
#            print(f'-------------------collecting stop--------------------')
#            break
            
if __name__ == '__main__':
    main()