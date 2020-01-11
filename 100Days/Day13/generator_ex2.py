# yield后面不放任何东西

def my_generator(n):
    for i in range(n):
        temp = yield
        print(f'我是{temp}')

g=my_generator(5)

print(next(g))
print(next(g))
g.send(100)
print(next(g))
print(next(g))