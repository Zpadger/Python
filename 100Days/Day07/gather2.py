#向集合添加元素和从集合删除元素

set1 = {1,2,3,3,3,2}
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
#添加单个值
set1.add(4)
set1.add(5)
#添加值，有相同的键会直接替换成 update 的值
set2.update([11,12])
#删除单个值
set2.discard(5)
if 4 in set2:
    set2.remove(4)

# remove和discard的区别
# remove(...)
#
# Remove an element from a set; it must be a member.
#
# If the element is not a member, raise a KeyError.
#
#
#
# discard(...)
#
# Remove an element from a set if it is a member.
#
# If the element is not a member, do nothing.

print(set1,set2)
print(set3)
print(set3.pop())#pop删除的特殊性
print(set3)