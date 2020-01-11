# StopIteration本质上是一个类，所以可以通过访问它的value属性获取这个return返回的值

def g3():
    yield 'a'
    return '这是错误说明'
    yield 'b'
g=g3()

try:
    print(next(g))  #a
    print(next(g))  #触发异常
except StopIteration as exc:
    result=exc.value
    print(result)