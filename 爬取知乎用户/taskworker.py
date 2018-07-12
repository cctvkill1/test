# -*- coding : utf-8 -*-
# task.py for windows

import time, sys, queue, random
from multiprocessing.managers import BaseManager

def test():
    try:
        BaseManager.register('get_task')

        conn = BaseManager(address = ('127.0.0.1',5000), authkey = b'123');

        conn.connect()
    except:
        print('连接失败')
        return 

    task = conn.get_task();

    while not task.empty():
        url = task.get(timeout=1); 
        print('run task %s...' % (url)) 

        time.sleep(1)

    print('work over')

if __name__ == '__main__':
    while True:
        test()
        time.sleep(1)