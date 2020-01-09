# 使用Queue实现进程间的通信
# 暂时没有解决方法

from multiprocessing import Process
from multiprocessing import Queue
from time import time,sleep

counter = 0

def sub_task(q):
    global counter
    while counter<10:
        print(q,end='',flush=True)
        counter += 1
        sleep(0.01)

def main():
    q = Queue()
    p1 = Process(target=sub_task,args=('Ping',))
    p2 = Process(target=sub_task,args=('Pong',))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

if __name__ == '__main__':
    main()