# # 最简单的生成器
# def my_generator(n):
#     for i in range(n):
#         yield i

# send()方法的使用
def my_generator(n):
    for i in range(n):
        temp = yield i
        print(f'我是{temp}')

g = my_generator(5)

print(next(g)) #输出0
print(next(g)) #输出1

g.send(100)    #本来输出2，但是传入新的值100，改为输出100

print(next(g)) #输出3
print(next(g)) #输出4