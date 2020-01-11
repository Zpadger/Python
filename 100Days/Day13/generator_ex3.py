# 生成器的启动

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

g = my_generator()
g.send(None)   #第一次启动，本来第一次应该迭代的1，这里被取代了，但是send(None)会返回1
print(next(g))
print(next(g))
print(next(g))