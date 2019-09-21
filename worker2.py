#Created on 9/20/2019 Friday
# -*- coding : utf-8 -*-
#@author: Raymond Jing
import time, sys, queue, random
from multiprocessing.managers import BaseManager

BaseManager.register('get_task')
BaseManager.register('get_result')
conn = BaseManager(address = ('127.0.0.1',8000), authkey = b'jr198868')


try:
    conn.connect()
except:
    print('Connect failed')
    sys.exit()
task = conn.get_task()
result = conn.get_result()


while not task.empty():
    n = task.get(timeout = 1)
    
    a = 1
    for i in range(1,n+1):
        a = a * i
    print('run task %d' % n)
    print(a)
    
    sleeptime = random.randint(0,3)
    time.sleep(sleeptime)
    rt = (n, sleeptime)
    result.put(rt)
if __name__ == '__main__':
    pass