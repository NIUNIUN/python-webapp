#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 协程：微线程 Coroutine
'''
子线程调用通过栈实现，一个线程就是执行一个子程序。
协程与子程序不同：
    在执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回接着执行。

特点： 一个线程执行。
优点：1、协程具有极高的执行效率。
      2、不需要多线程的锁机制。
实现：通过generator实现。

利用多核CPU：最简单的方法-- 多进程+协程
            既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

yield：不但可以返回一个值，还可以接受调用者发出的参数。
        send(argms)

'''

# 生产者-消费者
def consumer():
    r=''
    while True:
        # 2.consumer通过yield拿到传递的None，yield跳出
        n = yield r    # 生成器默认返回值为：None

        # 4.从上次跳出的位置，接着往下执行
        if not n:     # 当None时返回
            return    # 终止代码块，没有终止函数。相当于continue

        print('[consumer] Consuming %s...' % n)
        r = '200 OK'
        # 6.从这里开始循环，到yield的时候，再跳出来


def producer():
    # 1.启动生成器，会跳到consumer
    c.send(None)   #  send(None)等同于next()

    # 3.接着往下执行，产生数据，通过c.send(n)，再切换到consumer
    n =0
    while n < 5:
        n = n+1
        print('[proodcer] Producing %s...' % n)
        r = c.send(n)

        # 7.跳出来后，函数返回值是200 OK，所以往下执行，print出200 OK
        print('[producer] Consumer return: %s' % r)
        # 8.从这里开始循环前面的步骤，直到最后
    #
    c.close()

c = consumer()
producer()

'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

1.首先调用c.send(None)启动生成器；

2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

3.consumer通过yield拿到消息，处理，又通过yield把结果传回；

4.produce拿到consumer处理的结果，继续生产下一条消息；

5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”
'''

'''
 关于send()
http://blog.csdn.net/hedan2013/article/details/56293173
http://blog.csdn.net/iPenX/article/details/78096180
'''

'''
函数遇到 return x 会直接返回（退出该函数），没写 return x 就意味着函数最后一行默认有个 return None，
协程就是利用 yield 不会立马返回（退出）的特点，它会记录当前函数的状态，以便暂时离开后再次回到函数继续执行。
'''