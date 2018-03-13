#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'分布式进程'

import time,sys,queue
from multiprocessing.managers import BaseManager

# 客户端

class QueueManger(BaseManager):
    pass

def start_client():
    # 从网络上获取Queue，注册时只写入名字
    QueueManger.register('get_task_queue')
    QueueManger.register('get_result_queue')

    # 连接服务器
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    man = QueueManger(address=(server_addr,5000),authkey=b'abc')
    # 从网络连接
    man.connect()

    # 获取网络上注册过的queue
    task = man.get_task_queue()
    result = man.get_result_queue()

    # 从task队列中取出任务，并写入到result队列中
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n,n))
            r =  '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty')

    # 处理结束：
    print('worker exit...')

if __name__ == '__main__':
    start_client()