# 异步I/O操作 - asyncio模块
# 暂时没懂
import asyncio
import threading

@asyncio.coroutine  # 协程
def hello():
    print('%s: Hello,wolrd!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有yield from才会等待休眠操作执行完成
    yield from asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye,world!' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()