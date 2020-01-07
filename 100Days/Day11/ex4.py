# 引发异常和异常栈

def f1():
    raise AssertionError('发生异常')
    # 当程序出错时,python会自动触发异常,也可以通过raise显示引发异常
    # 一旦执行了raise语句,raise之后的语句不在执行
    # 如果加入了try,except,那么except里的语句会被执行

def f2():
    f1()

def f3():
    f2()

f1()
f2()
f3()