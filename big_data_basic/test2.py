import collection_sever as cs
import psutil

con = cs.CollectionSever('127.0.0.1',9999)
con.sever_run(11111)
#con.sever_run(psutil.cpu_percent(interval=0))