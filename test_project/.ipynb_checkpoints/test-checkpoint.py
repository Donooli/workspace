import multiprocessing as mp
from multiprocessing import Process
from threading import Timer

def cpu_timer():
    print("cpu :",psutil.cpu_percent(interval=1))
    a = threading.Timer(1,cpu_timer)
    a.start()

def ram_timer():
    print("ram :",psutil.virtual_memory().percent)
    a = threading.Timer(5,ram_timer)
    a.start()

def disk_timer():
    print("disk :",psutil.disk_usage("c://").percent)
    a = threading.Timer(60,disk_timer)
    a.start()

if __name__ == "__main__":
    p1 = mp.Process(target = cpu_timer)
    p2 = mp.Process(target = ram_timer)
    p3 = mp.Process(target = disk_timer)

    p1.deamon = True
    p2.deamon = True
    p3.deamon = True

    try:
        p1.start()
        p2.start()
        p3.start()
    except KeyboardInterrupt as e:
        print("------------end------------")
    