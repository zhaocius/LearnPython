#线程安全
from time import sleep
from threading import Thread,currentThread,Lock
from random import randint

class Account(object):
    def __init__(self):
        self.__count=0
        self.__lock=Lock()

    def add(self):
        self.__lock.acquire()
        try:
            self.__count+=1
        finally:
            self.__lock.release()
    def print(self):
        print('count == %d'%(self.__count))

class AddThread(Thread):
    def __init__(self,account):
        super().__init__()
        self.__account=account
    def run(self):
        self.__account.add()
        print(currentThread(),'add down')

def main():
    threads=[]
    account=Account()
    for _ in range(100):
        t=AddThread(account)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    account.print()

if __name__ == '__main__':
    main()

