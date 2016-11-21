# -*- coding : utf-8 -*-
# task.py for windows

import time, sys, queue, random
from multiprocessing.managers import BaseManager

def test():
    BaseManager.register('get_task')
    BaseManager.register('get_result')

    conn = BaseManager(address = ('127.0.0.1',5000), authkey = b'123');

    try:
        conn.connect();
    except:
        print('连接失败');
        sys.exit();

    task = conn.get_task();
    result = conn.get_result();

    while not task.empty():
        n = task.get(timeout = 1); 
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n) 
        result.put(r) 
        # sleeptime = random.randint(0,3);
        # time.sleep(sleeptime);
        # rt = (n, sleeptime); 

    print('work over')

if __name__ == '__main__':
    test()