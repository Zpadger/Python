# 将这个任务分解到8个进程中去执行
# 暂时也不考虑列表切片操作花费的时间
# 只是把做运算和合并运算结果的时间统计出来

from multiprocessing import Process,Queue
from random import randint
from time import time

def task_handler(curr_list,result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processs = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index+12500000],result_queue))
        index += 12500000
        processs.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processs:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time:',(end-start),'s',sep='')

if __name__ == '__main__':
    main()

# 5000000050000000
# Execution time:0.3451664447784424s