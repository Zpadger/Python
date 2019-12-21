#正整数的反转

num = int(input('num='))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num*10 + num % 10
    num //= 10
print('经过翻转后的数字为：%d'%(reversed_num))
