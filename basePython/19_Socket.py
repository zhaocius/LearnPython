from socket import socket,SOCK_STREAM,AF_INET
from threading import Thread
from time import sleep

def server():
    server=socket(family=AF_INET,type=SOCK_STREAM)
    server.bind(('127.0.0.1',8888))
    server.listen(512)
    while True:
        client,addr=server.accept()
        sleep(1)
        print(str(addr),'连接服务器')
        client.send(("hello"+str(addr)).encode('utf-8'))
        client.close()

def client():
    client =socket()
    client.connect(('127.0.0.1',8888))
    print(client.recv(1024).decode('utf-8'))
    client.close()

def main():
    print('a')
    t1=Thread(target=server)
    t1.start()
    sleep(2)
    client()

if __name__ == '__main__':
    main()




