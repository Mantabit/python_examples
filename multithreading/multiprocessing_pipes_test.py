import multiprocessing as mp
import time

class testClass(object):
    def __init__(self,name):
        self.name=name
    def doSomething(self):
        print("Object %s reporting!"%(self.name))

#this function will run in another process and receives a queue as argument
#over which it can receive an object from the parent process        
def workerFunction(receive_end):
    #receive object from the queue (blocking call)
    obj=receive_end.recv()
    #use the received object
    obj.doSomething()
    
if __name__=="__main__":
    (receive_end,send_end)=mp.Pipe()
    
    p=mp.Process(target=workerFunction,args=[receive_end])
    p.start()
    
    time.sleep(3)
    
    send_end.send(testClass("John"))
    
    #close the queue from the main thread, indicating no more data will flow from main thread
    send_end.close()

    #wait for the worker process to finish
    p.join()