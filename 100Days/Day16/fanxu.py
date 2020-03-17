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