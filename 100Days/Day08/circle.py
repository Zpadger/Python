# 练习
# 修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
# 过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
# 输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

import math

class Circle(object):
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,radius):
        self._radius = radius if radius > 0 else 0
    # setter装饰器必须在property的后面，且两个被修饰的属性（函数）名称必须保持一致
    # 该装饰器允许你对已用@property装饰的属性（函数）赋值
    # 注意啦：@property是把一个函数变成属性，*.setter是给@property修饰的函数赋值，这两个装饰器修饰的函数名是一样的

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius

if __name__ == '__main__':
    radius = float(input('请输入游泳池的半径：'))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('围墙的造价为：￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为：￥%.1f元' % ((big.area - small.area) * 65))