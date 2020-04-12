# 华为2019暑期实习笔试题
# 第一题
# 题意
#    给出一个字符串，由许多子串组成，每个子串长度都是9
#    如果子串的第一位是0，就将该子串反序输出
#    如果子串的第一位是1，就将该子串正序输出


def main():
    s = input("输入字符串:")
    l = len(s)
    n = int(l / 9)
    i = j = 0
    while j < n:
        t = s[i:i+9]
        i += 9
        j += 1
        if t[0] == '0':
            print(t[::-1])
        if t[0] == '1':
            print(t)

if __name__ == '__main__':
    main()