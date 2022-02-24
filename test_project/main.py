import time
import psutil

start_time = int(time.time())
time_cache = start_time
while 1:
    try:
        now_time = int(time.time())
        if time_cache != now_time:
            time_cache = now_time
            time_gap = now_time - start_time
            if time_gap % 1 == 0:
                print('cpu :',psutil.cpu_percent(interval=1),'%')
            if time_gap % 5 == 0:
                print('RAM :',round(((psutil.virtual_memory().total - psutil.virtual_memory().free) / psutil.virtual_memory().total * 100),1),'%')
            if time_gap % 60 == 0:
                print('disk :',round(((psutil.disk_usage('C://').total - psutil.disk_usage('C://').free) / psutil.disk_usage('C://').total * 100),1),'%')
            print('------------------------------------')
    except KeyboardInterrupt as e:
        print('----------------STOP----------------')
        break
