# 下面的代码实现了一个提供时间日期的服务器

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():

    server = socket(family=AF_INET, type=SOCK_STREAM)

    server.bind(('127.0.0.1',6789))


    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')

        client.send(str(datetime.now()).encode('utf-8'))
        client.close()

if __name__ == '__main__':
    main()

# Mac中没有Windows自带的telnet客户端
# # 需要安装
# # brew install telnet
# 查询本机IP地址 ifconfig

# 上面的服务器并没有使用多线程或者异步I/O的处理方式
# 这也就意味着当服务器与一个客户端处于通信状态时，其他的客户端只能排队等待
