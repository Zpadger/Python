## 创建集合的字面量语法

set1 = {1,2,3,3,3,2}
print(set1)
print('Length=',len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1,10))
set3 = set((1,2,3,3,2,1))
print(set2,set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1,100) if num % 3 == 0 or num % 5 == 0}
print(set4)