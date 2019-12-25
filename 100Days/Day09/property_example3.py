#如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作
#使用@property包装器来包装getter和setter方法

class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('张三',12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '李四'
    # AttributeError: can't set attribute

if __name__ == '__main__':
    main()
