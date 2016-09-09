import threading
 
class mythread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global event
        if event.isSet():
            event.clear()
            event.wait()
            print self.getName()
        else:
            print self.getName()
            event.set()
event=threading.Event()
event.set()
t1=[]
for i in range(10):
    t=mythread(str(i))
    t1.append(t)
 
for i in t1:
    i.start()