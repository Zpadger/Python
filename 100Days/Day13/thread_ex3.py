# 多个线程共享数据 - 无锁的情况
# 一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”

from time import sleep
from threading import Thread

class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self,money):
        # 计算存款后的余额
        new_balance = self._balance + money
        # 模拟受理存款业务需要0.01秒的时间
        sleep(0.01)
        # 修改账户余额
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为:$%d元' % account.balance)

if __name__ == '__main__':
    main()

# 运行上面的程序，结果让人大跌眼镜，100个线程分别向账户中转入1元钱
# 结果居然远远小于100元。之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护
# 多个线程同时向账户中存钱时，会一起执行到new_balance = self._balance + money这行代码
# 多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，因此得到了错误的结果
