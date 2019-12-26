# 子类在继承了父类的方法后
# 可以对父类已有的方法给出新的实现版本
# 这个操作称之为方法重写（override）
# 通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本
# 当我们调用这个经过子类重写的方法时
# 不同的子类对象会表现出不同的行为
# 这个就是多态（poly-morphism）

from abc import ABCMeta, abstractclassmethod

class Pet(object,metaclass=ABCMeta):
    def __init__(self,nickname):
        self._nickname = nickname

    @abstractclassmethod
    #cls or self?
    def make_voice(cls):
        pass

class Dog(Pet):
    # 狗
    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)

class Cat(Pet):
    # 猫
    def make_voice(self):
        print('%s:喵呜~喵呜~' % self._nickname)

def main():
    pets = [Dog('狗子'),Cat('喵唧'),Dog('阿黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
