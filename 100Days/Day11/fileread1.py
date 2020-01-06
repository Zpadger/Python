# 读取一个纯文本文件

def main():
    f =open('123.txt','r',encoding='utf-8')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()
