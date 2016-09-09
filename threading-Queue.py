# coding=utf-8
#测试utf-8编码
from multiprocessing import Queue
from threading import Thread
# from single import *
import sys
import time  

# reload(sys)
# sys.setdefaultencoding('utf-8')


class ProcessWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue
            num = self.queue.get()
            processNum(num)
            self.queue.task_done()


def main():
    ts = time()
    nums = getNums(4)
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 4 worker threads
    # 创建四个工作线程
    for x in range(4):
        worker = ProcessWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        # 将daemon设置为True将会使主线程退出，即使worker都阻塞了
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue
    for num in nums:
        queue.put(num)
    # Causes the main thread to wait for the queue to finish processing all the tasks
    # 让主线程等待队列完成所有的任务
    queue.join()
    print("cost time is: {:.2f}s".format(time() - ts))


if __name__ == "__main__":
    main()