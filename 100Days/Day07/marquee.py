#动态弹幕

import os
import _thread, time
from pip._vendor.distlib.compat import raw_input

def input_thread(L):
    raw_input()
    L.append(None)

def main():
    L = []
    _thread.start_new_thread(input_thread,(L,))
    str = 'Welcome to Huazhong University of Science and Technology      '
    #counter = 0
    while True:
        if L : break
        print(str)
        #counter += 1
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for Windows use os.system('cls') instead
        os.system('clear')
        # if counter == 100:
        #     break

if __name__ == '__main__':
    main()
