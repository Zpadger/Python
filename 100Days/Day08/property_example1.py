#对属性的操作

# class Rectangle(object):
#     def __init__(self):
#         self.width =10
#         self.height=20
# r=Rectangle()
# print(r.width,r.height)
# 此时输出结果为10 20

#但是这样在实际使用中会产生一个严重的问题，__init__ 中定义的属性是可变的
# 换句话说，是使用一个系统的所有开发人员在知道属性名的情况下，可以进行随意的更改(尽管可能是在无意识的情况下)
# 但这很容易造成严重的后果

# class Rectangle(object):
#     def __init__(self):
#         self.width =10
#         self.height=20
# r=Rectangle()
# print(r.width,r.height)
# r.width=1.0
# print(r.width,r.height)
# 以上代码结果会输出宽1.0，可能是开发人员不小心点了一个小数点上去
# 但是会系统的数据错误，并且在一些情况下很难排查

#将width属性设置为私有的，其他人不能随意更改的属性，如果想要更改只能依照我的方法来修改
# @property就起到这种作用(类似于java中的private)
class Rectangle(object):
    @property
    def width(self):
        #变量名不与方法名重复，改为true_width，下同
        return self.true_width

    @property
    def height(self):
        return self.true_height

s = Rectangle()
#与方法名一致
s.width = 1024
s.height = 768
print(s.width,s.height)
# 此时，如果在外部想要给width重新直接赋值就会报错：
# s.width = 1024
# AttributeError: can't set attribute