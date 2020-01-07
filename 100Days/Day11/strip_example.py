# strip()函数介绍

t = '123'

a = ' 123 '
print(a)
# s.strip(rm) 删除s字符串中开头、结尾处
print('%s%s' % (a.strip(),t))

# s.lstrip(rm) 删除s字符串中开头处
print('%s%s' % (a.lstrip(),t))

# s.rstrip(rm) 删除s字符串中结尾处
print('%s%s' % (a.rstrip(),t))