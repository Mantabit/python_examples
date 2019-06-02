import multiprocessing as mp
import time

class testClass(object):
    def __init__(self,name):
        self.name=name
    def doSomething(self):
        print("Object %s reporting!"%(self.name))

#function receives objects      
def receiverFunction(receive_end):
    while True:
        #receive object from the pipe
        try:
            obj=receive_end.recv()
        except EOFError as err:
            print("nothing left in the queue, aborting receiver thread")
            break
        #use the received object
        obj.doSomething()

#function generates objects   
def producerFunction(send_end):
    start=time.time()
    i=0
    #produce data every 50ms for 5s
    while time.time()-start<1:
        i+=1
        send_end.send(testClass("Object%d"%(i)))
        time.sleep(50e-3)
    print("Closing the send_end in producer process...")
    send_end.close()
    
if __name__=="__main__":
    (receive_end,send_end)=mp.Pipe()
    
    p_recv=mp.Process(target=receiverFunction,args=[receive_end])
    p_send=mp.Process(target=producerFunction,args=[send_end])
    p_recv.start()
    p_send.start()
    
    p_send.join()
    send_end.close()
    print("Closing send_end in parent process")
    p_recv.join()