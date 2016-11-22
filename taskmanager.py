#!/usr/bin/env python3
# -*- coding : utf-8 -*- 

import time,queue,random
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#任务个数
task_number = 10;

#定义收发队列
task_queue = queue.Queue(task_number);
result_queue = queue.Queue(task_number);

def gettask():
    return task_queue;
def getresult():
     return result_queue;

def test():
    #windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    BaseManager.register('get_task',callable = gettask);
    BaseManager.register('get_result',callable = getresult);
    #绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地
    manager = BaseManager(address = ('127.0.0.1',5000),authkey = b'123');
    #启动
    manager.start();
    try:
        #通过网络获取任务队列和结果队列
        task = manager.get_task();
        result = manager.get_result();

        #添加任务
        for i in range(task_number):
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n);

        #每秒检测一次是否所有任务都被执行完
        while not result.full():
            time.sleep(1);

        for i in range(result.qsize()): 
            r = result.get(timeout=10)
            print('Result: %s' % r)

        print('all over')
        
    
    except Exception as e:
        print('Manager error:',e);
    finally:
        #一定要关闭，否则会爆管道未关闭的错误
        time.sleep(1);
        manager.shutdown();
        
if __name__ == '__main__':
    #windows下多进程可能会炸，添加这句可以缓解
    freeze_support()
    test();