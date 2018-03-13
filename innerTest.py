#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'常用内置模块'
import datetime,re
now = datetime.datetime.now()
print('当前时间',now)
print(type(now))

# 指定日期、时间
dt = datetime.datetime(2015,12,28,19,48,38)
print('\n获取指定日期和时间',dt)

# 计算机存储时间单位：timestamp，浮点数，小数位表示毫秒
print('timestamp=',dt.timestamp())

# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
t = datetime.datetime.fromtimestamp(142941720.00)
print('\ntimestamp转换为datetime=',t)

# 本地时间是指当前操作系统设定的时区
# 实际上就是UTC+8:00时区的时间：
# 2015-04-19 12:20:00 UTC+8:00

print('UTC时间=',datetime.datetime.utcfromtimestamp(142941720.00))


# str转换为datetime
cday = datetime.datetime.strptime('2015/6/1 18-19-59', '%Y/%m/%d %H-%M-%S')
print('\n转换为datetime',cday)

cStr = datetime.datetime.strftime(datetime.datetime.now(),'%a %b %d %H:%M')
print('\n转换为str=',cStr)


# datetime加减  一个timedalta对象代表了一个时间差
now = datetime.datetime.now()
print('datetime加',now + datetime.timedelta(hours =10))
print('datetime减',now - datetime.timedelta(hours =10))

print('datetime日期加',now + datetime.timedelta(hours =10,days=1))



# 本地时间转换UTC时间
tz_utc_8 = datetime.timezone(datetime.timedelta(hours=-7))
print('\nUTC+7 =',now)
print('\nUTC+7 =',now.replace(tzinfo=tz_utc_8))   # replace 只是更换时区，时分秒不会发生变化
print('\nUTC+7 =',now.astimezone(tz_utc_8))       # 时区间进行切换，发生变化

# 时区转换utcnow()
tz_utc = datetime.timezone.utc
utc_dt = datetime.datetime.utcnow()   # 获取UTC时间
print('\nutc时区=',tz_utc)
print('utc时间',utc_dt,'强制添加时区为UTC',datetime.datetime.utcnow().replace(tzinfo=tz_utc))

bj_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
print('北京时间',bj_dt)
tokyo_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
print('东京时间',tokyo_dt)

tokyo_dt2 =  bj_dt.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
print('北京时间转换为东京时间 %s \n\n' % tokyo_dt2)


# 练习 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
# to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
def to_timestamp(dt_str,tz_str):
    # 提取时区
    m_tzone = re.match(r'UTC([+-]{1}\d{1,2}):\d{2}',tz_str)
    # 将str转换为datetime
    dt = datetime.datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    # 设置时区
    tz = datetime.timezone(datetime.timedelta(hours=int(m_tzone.group(1))))
    # dtime = dt.astimezone(tz)  # 1433117430.0 dt= 2015-06-01 08:10:30      1433059830.0 dt= 2015-05-31 16:10:30
    dtime = dt.replace(tzinfo=tz)  # 1433121030.0 dt= 2015-06-01 09:10:30    1433121030.0 dt2= 2015-06-01 09:10:30
    return dtime.timestamp()
    # return dtime

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
print('练习',t1,'dt2=',datetime.datetime.fromtimestamp(t1))

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
assert t2 == 1433121030.0, t2
print('练习',t2,'dt2=',datetime.datetime.fromtimestamp(t2))
print('OK!')


# 系统提供了datetime.astimezone(tz)方法，使用这个方法可以在各个时区之间来回转换时间。这里有两点需要注意：

# 如果datetime对象本身没有包含时区信息，调用这个方法会抛出ValueError，并提示astimezone() cannot be applied to a naive datetime
# replace(tzinfo=...)方法只会替换tzinfo的值，并不会更改时分秒等时间信息
