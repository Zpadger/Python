# 生成器的关闭

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

g = my_generator()
print(next(g))
print(next(g))
g.close()
print(next(g))   #在此处会显示错误
print(next(g))