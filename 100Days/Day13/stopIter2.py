# 如果遇到return,如果在执行过程中 return，则直接抛出 StopIteration 终止迭代

def g2():
    yield 'a'
    return
    yield 'b'
g=g2()
next(g)    #程序停留在执行完yield 'a'语句后的位置。
next(g)    #程序发现下一条语句是return，所以抛出StopIteration异常，这样yield 'b'语句永远也不会执行。
