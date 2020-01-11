# 在一个生成器中，如果没有return，则默认执行到函数完毕时返回StopIteration

def g1():
    yield 1
g=g1()
next(g)    #第一次调用next(g)时，会在执行完yield语句后挂起，所以此时程序并没有执行结束。
next(g)    #程序试图从yield语句的下一条语句开始执行，发现已经到了结尾，所以抛出StopIteration异常。