import multiprocessing as mp
import time

class testClass(object):
    def __init__(self,name):
        self.name=name
    def doSomething(self):
        print("Object %s reporting!"%(self.name))

#this function will run in another process and receives a queue as argument
#over which it can receive an object from the parent process        
def workerFunction(q):
    #receive object from the queue (blocking call)
    obj=q.get()
    #use the received object
    obj.doSomething()
    
if __name__=="__main__":
    queue=mp.Queue()
    
    p=mp.Process(target=workerFunction,args=[queue])
    p.start()
    
    time.sleep(3)
    
    queue.put(testClass("John"))
    
    #close the queue from the main thread, indicating no more data will flow from main thread
    queue.close()
    
    queue.join_thread()
    #wait for the worker process to finish
    p.join()