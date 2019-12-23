#使用列表的生成式语法来创建列表
import sys

# 用列表的生成表达式语法创建列表容器
f = [x for x in range(1,10)]
print(sys.getsizeof(f))
print(f)
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x+y for x in 'ABCDE' for y in '1234567']
print(sys.getsizeof(f))
print(f)

f = [x**2 for x in range(1,10)]#1000
# 查看对象占用内存的字节数
print(sys.getsizeof(f))
print(f)

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x**2 for x in range(1,10))#1000
# 相比生成式生成器不占用存储数据的空间
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)