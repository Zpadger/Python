# 生成器 - 生成器语法

seq = [x * x for x in range(10)]
print(seq)
# x = [x for x in range(10)]
# for x,y in zip(x,seq):
#     print(x,y)

gen = (x * x for x in range(10))
print(gen)
# <generator object <genexpr> at 0x7ffb25f7ccd0>
for x in gen:
    print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)
# <generator object <genexpr> at 0x7ffb25f7cd50>
n = 1
while n < num:
    print(next(gen))
    n += 1