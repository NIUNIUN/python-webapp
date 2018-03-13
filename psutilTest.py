#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# psutil = process and system utilities
# 实现系统监控
import psutil


# 获取CPU信息
count = psutil.cpu_count()
print('CPU逻辑数量',count)
print('CPU物理核心',psutil.cpu_count(logical=False))
# 2说明是双核超线程, 4则是4核非超线程

# 统计CPU的用户／系统／空闲时间：
print('\n',psutil.cpu_times())

for x in range(5):
    print('\ncpu总使用率 %s 单个CPU使用率%s' % (psutil.cpu_percent(interval=1,percpu=False),psutil.cpu_percent(interval=1,percpu=True)))
# percpu默认为False，总的使用率
# interval -- 每隔多少秒，刷新一次; percpu则指定是选择总的使用率还是每个cpu的使用率


# 内存信息
print('\n物理内存 ',psutil.swap_memory())
print('交换内存 ',psutil.virtual_memory())


# 磁盘信息
print('\n\n磁盘IO ',psutil.disk_io_counters())
print('\n磁盘使用情况 ',psutil.disk_usage('/'))

print('\n磁盘分区 ',psutil.disk_partitions())
# decide-分区  mountpoint-挂载点 fstype-文件系统格式 opts-挂载参数 中包含rw表示可读写，journaled表示支持日志。


# 网络信息
print('\n\n',psutil.net_io_counters())  #网络读写字节/包的个数
print('\n信息',psutil.net_if_addrs())   #网络接口信息
print('\n状态',psutil.net_if_stats())   #网络接口状态
print('\n当前连接状态',psutil.net_connections())



# AccessDenied错误：原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：


# 进程信息
print('\n\n所有进程 ',psutil.pids())
p = psutil.Process(5712)  #指定进程
print('\n[5712]name = ',p.name())
print('[5712] = ',p.exe())
print('[5576]工作目录 = ',p.cwd())
print('[5576]命令行 = ',p.cmdline())
print('[5576]命令行 = ',p.cmdline())
print('[5576]父进程 = ',p.parent())
print('[5576]父进程ID = ',p.ppid())
print('[5576]子进程ID = ',p.children())
print('[5576]进程状态 ',p.status())
print('[5576]进程用户名 ',p.username())
# print('[5568]进程终端 ',p.terminal())
print('[5576]cpu时间  ',p.cpu_times())
print('[5576]内存  ',p.memory_info())
print('[5576]打开文件  ',p.open_files())
print('[5576]相关网络连接  ',p.connections())
print('[5576]线程  ',p.threads())
print('[5576]线程数量  ',p.num_threads())
print('[5576]环境变量  ',p.environ())
# print('[5576]结束进程  ',p.terminate())




# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
print('\n',psutil.test())





