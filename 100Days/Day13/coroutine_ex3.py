# yield实现协程的例子
# 数字模型

def average():
    total = 0.0    #数字的总和
    count = 0      #数字的个数
    avg = None     #平均值
    while True:
        num = yield avg
        total += num
        count += 1
        avg = total/count

#定义一个函数，通过这个函数向average函数发送数值
def sender(generator):
    print(next(generator))  #启动生成器
    print(generator.send(10))   # 10
    print(generator.send(20))   # 20
    print(generator.send(30))   # 30
    print(generator.send(40))   # 40

g = average()
sender(g)