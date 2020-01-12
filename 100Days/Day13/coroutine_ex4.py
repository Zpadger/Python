# 查看协程的状态

from inspect import getgeneratorstate
from time import sleep

def my_generator():
    for i in range(3):
        sleep(0.5)
        x = yield i + 1

g = my_generator()

def main(generator):
    try:
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        next(g)  # 激活生成器
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        g.send(100)
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        next(g)
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))
        next(g)
    except StopIteration:
        print('全部迭代完毕了')
        print("生成器初始状态为:{0}".format(getgeneratorstate(g)))

if __name__ == '__main__':
    main(g)