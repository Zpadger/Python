#字符串操作

s1 = 'hello,world!'
s2 = "hello,world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello,
world!
"""

print(s1,s2,s3,end='')

#使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义
s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'
print(s1,s2,end='')

#不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u4F60\u597D'
print(s1, s2)