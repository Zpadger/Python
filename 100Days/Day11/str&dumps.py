import json
print(str([1,2])) # [1, 2]
print(str([1, 2]))
print(str([1,  2]))
print(str([1,2]) == str([1, 2]) == str([1,  2])) # True

print(json.dumps([1,2])) #[1, 2]
print(json.dumps([1, 2]))
print(json.dumps([1,  2]))
print(json.dumps([1,2]) == json.dumps([1, 2]) == json.dumps([1,  2])) # True

# str和json.dumps都不是原模原样地输出我们输入的内容，会自动将列表逗号后面只加一个空格
# 在[1, 2]这个例子上，二者是一样的

# 引号

print(str(['a', 'b'])) # ['a', 'b']
print(json.dumps(['a', 'b'])) # ["a", "b"]
print(json.dumps(['a', 'b']) == str(['a', 'b'])) # False

print(str({'a': 1})) # {'a': 1}
print(json.dumps({'a': 1})) # {"a": 1}
print(json.dumps({'a': 1}) == str({'a': 1})) # False

# str转化后的字符串中，引号是用单引号
# 而json.dumps是双引号，这在字典和列表中都是这样

# 布尔值

print(str([True, False])) # '[True, False]'
print(json.dumps([True, False])) # '[true, false]'
print(json.dumps([True, False]) == str([True, False])) # False

# str转化后的字符串中，True是首字母大写的
# 而json.dumps将所有字母都转化为了小写

# None

print(str([1, None])) # '[1, None]'
print(json.dumps([1, None])) # '[1, null]'
print(json.dumps([1, None]) == str([1, None])) # False

# str转化后的字符串中，None还是用None表示
# 而json.dumps则用null表示

# 我们都知道，使用json.dumps的目的是将python对象转化为字符串，以存储到文件之中
# 之后需要数据的时候还要从文件中读取，再用json.loads转化为python对象，类似下面这个过程

m = ['a', 'b']
n = json.dumps(m)
print(n) # ["a", "b"]

# -----存储入文件，读取文件-----
p = json.loads(n)
p.append('c')
print(p) # ['a', 'b', 'c']

# 如果用str转化成的字符串，则无法通过json.dumps转化为python对象

m = ['a', 'b']
n = str(m)
print(n) # "['a', 'b']"
print(json.loads(n)) # 无输出

# 也就是说str转化出的字符串格式不符合json规范，无法完成json格式字符串与python对象之间的转换
# (但是可以使用eval函数转换)