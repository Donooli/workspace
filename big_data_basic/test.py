import collection_sever as cs
import time

con = cs.CollectionSever('127.0.0.1', 9999)
con.sever_run(f'{time.process_time()}')

