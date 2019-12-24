#定义和使用时钟类

import time
import os
import _thread, time
from pip._vendor.distlib.compat import raw_input
#新加入了按键回车停止死循环的功能

class Clock(object):

    def __init__(self,**kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self.second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def input_thread(L):
    raw_input()
    L.append(None)

if __name__ == '__main__':
    clock =  Clock()
    L = []
    _thread.start_new_thread(input_thread, (L,))
    while True:
        os.system('clear')
        if L: break
        print(clock.show())
        time.sleep(1)
        clock.run()

# import _thread, time
# from pip._vendor.distlib.compat import raw_input
#
# def input_thread(L):
#     raw_input()
#     L.append(None)
#
# def do_print():
#     L = []
#     _thread.start_new_thread(input_thread, (L,))
#     while 1:
#         time.sleep(.1)
#         if L: break
#         print("Hi Mom!")
#
# #do_print()
# if __name__ == '__main__':
#     do_print()