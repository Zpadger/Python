#动态弹幕

import os
import time

def main():
    str = 'Welcome to Huazhong University of Science and Technology      '
    counter = 0
    while True:
        print(str)
        counter += 1
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for Windows use os.system('cls') instead
        os.system('clear')
        if counter == 100:
            break


if __name__ == '__main__':
    main()