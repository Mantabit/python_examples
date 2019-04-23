#!/usr/bin/python

import threading
from time import sleep

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        synchronizedPrint("Starting Thread: %s\n"%(self.name))
        for i in range(0,self.counter):
            synchronizedPrint("It's Thread: %s\n"%(self.name))
            sleep(0.05)
        synchronizedPrint("Exiting Thread %d\n"%(self.threadID))

# Create new threads
thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 5)

threadLock=threading.Lock()
def synchronizedPrint(message):
    threadLock.acquire()
    print(message)
    threadLock.release()

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting Main Thread")