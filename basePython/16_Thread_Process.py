#如果IO密集使用多线程
#由于GIL的存在，无法发挥CPU多核性能，计算密集型，使用多进程

from time import sleep,time
from threading import Thread
from random import randint

class DownloadThread(Thread):
    def __init__(self,filename):
        super().__init__()
        self.__filename=filename

    def run(self):
        print('start download %s' % (self.__filename))
        sleep(randint(5, 10))
        print('download done')

def download(filename):
    print('start download %s' %(filename))
    sleep(randint(5,10))
    print('download done')

#直接用thread类，也可以继承，复写run方法。
def main():
    start=time()
    t1=Thread(target=download,args=('wawa',))
    t1.start()
    t2=Thread(target=download,args=('haha',))
    t2.start()
    t1.join()
    t2.join()
    end=time()
    print('消耗了 %f 秒' %(end-start))

def main1():
    start=time()
    t1=DownloadThread('wawa')
    t2=DownloadThread('haha')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end=time()
    print('消耗了%.2f秒'%(end-start))

if __name__ == '__main__':
    main1()