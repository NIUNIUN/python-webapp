#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 知识点：分布式进程'

import random,time,queue
from multiprocessing.managers import BaseManager

# 服务端

# 发送任务的队列
task_queue =  queue.Queue()
# 接收结果队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def return_task_queue():
    # global task_queue
    return task_queue

def return_result_queue():
    # global result_queue
    return result_queue

def  start_server():
# QueueManager.register('get_task_queue',callable=lambda :task_queue)   匿名函数不支持序列化
# QueueManager.register('get_task_queue',callable=lambda :task_queue)

    # 注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)
    # 绑定IP、端口，验证码
    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    # 启动Queue
    manager.start()

    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 为什么是.get_task_queue()，而不是.get_task_queue

    # 放几个任务
    # 不能直接对原始task_queue操作，必须通过QueueManger获得queue
    for i in range(10):
        n = random.randint(0,10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列中取出结果
    print('Try get result...')
    for i in range(10):
        r = result.get(timeout = 100)  # 设置超时时长为100s
        print('Result: %s ' % r)

    # 关闭Queue
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    start_server()



# QueueManager.register('get_task_queue',callable=lambda :task_queue)
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
# 匿名函数不能序列化
