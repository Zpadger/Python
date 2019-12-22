#函数的定义和使用 - 计算组合数C(7,3)

m = int(input('m='))
n = int(input('n='))
fm = 1
for num in range(1,m+1):
    fm *= num
fn = 1
for num in range(1,n+1):
    fn *= num
fmn = 1
for num in range(1,m-n+1):
    fmn *= num
print(fm//fn//fmn)

#重构
#阶乘
def factoria(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input('m='))
n = int(input('n='))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(factoria(m)//factoria(n)//factoria(m-n))