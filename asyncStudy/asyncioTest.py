#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

'''

import asyncio,threading

@asyncio.coroutine   # 把generator标记为coroutine类型
def hello(n):
    print('Hello (%s) (%s)!' % (n,threading.current_thread()))

    # 异步调用asynic.sleep(1)
    r = yield from asyncio.sleep(n*10)
    # asyncio.sleep() 也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
    # 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。

    print('\nHello (%s) again! (%s)' % (n,threading.currentThread()))

# 获取EventLoop
loop = asyncio.get_event_loop()

# 执行coroutine
# task =[hello(1),hello(2),hello(3)]
# loop.run_until_complete(asyncio.wait(task))
# loop.close()

# yield from：方便调用另一个generator
'''
    把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
    而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
    如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
'''

# 练习：asyncio的异步网络连接来获取sina、sohu和163的网站首页：
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host,80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()   #刷新底层传输的写缓冲区。
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s ' % (host,line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
task = [wget(host) for host in  ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(task))
loop.close()

# 可见3个连接由一个线程通过coroutine并发完成。
'''
writer.drain()
https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter
刷新底层传输的写缓冲区。也就是把需要发送出去的数据，从缓冲区发送出去。
没有手工刷新，asyncio为你自动刷新了。
当执行到reader.readline()时，asyncio知道应该把发送缓冲区的数据发送出去了。
'''

'''
小结
asyncio提供了完善的异步IO支持；

异步操作需要在coroutine中通过yield from完成；

多个coroutine可以封装成一组Task然后并发执行。

'''