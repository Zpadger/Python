#提供了封装方法的方式进行属性的修改

class Rectangle(object):
    @property
    def width(self):
        # 变量名不与方法名重复，改为true_width，下同
        return self.true_width
    @width.setter
    def width(self,input_width):
        self.true_width = input_width

    @property
    def height(self):
        return self.true_height
    @height.setter
    # 与property定义的方法名要一致
    def height(self,input_height):
        self.true_height = input_height

s = Rectangle()
# 与方法名一致
s.width = 1024
s.height = 768
print(s.width,s.height)

# 删除操作
# @height.deleter
# def height(self):
#         del self.true_height
