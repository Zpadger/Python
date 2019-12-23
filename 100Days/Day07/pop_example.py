#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
a =[1,2,3,4,5]
print(a.pop())
print(a)

list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop()
print("删除的项为 :", list_pop)
print("列表现在为 : ", list1)

#当集合是由列表和元组组成时,set.pop()是从左边删除元素的
set1 = set([9, 4, 5, 2, 6, 7, 1, 8])
print(set1)
print(set1.pop())
print(set1)

set1 = set((6, 3, 1, 7, 2, 9, 8, 0))
print(set1)
print(set1.pop())