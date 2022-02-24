import time
import psutil
import collection_sever as cs

con = cs.CollectionSever('172.0.0.1',9999)

start_time = int(time.time())
time_cache = start_time
while 1:
    try:
        now_time = int(time.time())
        if time_cache != now_time:
            time_cache = now_time
            time_gap = now_time - start_time
            if time_gap % 1 == 0:
                print('cpu :',psutil.cpu_percent(interval=0),'%')
                con.sever_run(psutil.cpu_percent(interval=0))
            if time_gap % 5 == 0:
                print('RAM :',psutil.virtual_memory().percent,'%')
                con.sever_run(psutil.virtual_memory().percent)
            if time_gap % 60 == 0:
                print('disk :',psutil.disk_usage("c://").percent,'%')
                con.sever_run(psutil.disk_usage("c://").percent)

            print('------------------------------------')
    except KeyboardInterrupt as e:
        print('----------------STOP----------------')
        break