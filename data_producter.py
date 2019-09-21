# -*- coding : utf-8 -*-
#Created on 9/20/2019 Friday
# @author: Raymond Jing

import time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#number of tasks 
task_number = 100

#Define two queues for data sending and receiving 
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)

def gettask():
    return task_queue

def getresult():
     return result_queue

def test():
    #define get_task and get_result functions 
    BaseManager.register('get_task',callable = gettask)
    BaseManager.register('get_result',callable = getresult)
    
    #setup ip address and authorization key
    manager = BaseManager(address = ('127.0.0.1',8000),authkey = b'jr198868')
    
    #start the server
    manager.start()
    try:
        #Get tasks from task_queue and result_queue
        task = manager.get_task()
        result = manager.get_result()
        
        #adding tasks 
        for i in range(task_number):
            print('Put task %d...' % i)
            task.put(i)
        #Check if the task has been implemented
        while not result.full():
            time.sleep(1)
        for i in range(result.qsize()):
            ans = result.get()
            print('task %d is finish , runtime:%d s' % ans)
    
    except:
        print('Manager error')
    finally:
        manager.shutdown()
        
if __name__ == '__main__':
    freeze_support()
    test()