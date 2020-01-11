# 迭代器(生成器)的send方法

def my_generator(n):
    for i in range(n):
        yield i

g=my_generator(5)

print(next(g))
print(next(g))
# print(next(g))
g.send(100)

# a=g.send(100)
# # print('我是{0}'.format(a))
# print(f'我是{a}')

print(next(g))
print(next(g))

#我们发现虽然100传进去了，但是他并没有迭代出来，那原来的2去哪里了呢？
# send(100)实际上就是返回的2