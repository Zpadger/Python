# throw --raise exception in generator
# return next yielded value or StopIteration

def my_generator():
    yield 'a'
    yield 'b'
    yield 'c'

g=my_generator()
print(next(g))
print(next(g))
print('-------------------------')
print(g.throw(StopIteration))
print(next(g))
