# 如果在return后返回一个值，那么这个值为StopIteration异常的说明，不是程序的返回值

def g3():
    yield 'a'
    return '这是错误说明'
    yield 'b'   #有一些编辑器会提示错误，此处为unreachable code，即不可到达的代码
g=g3()
next(g)
next(g)