#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle,json

#  序列化：把变量从内存中变成可存储或传输的过程称之为序列化
d = dict(name='Bob',age=20,score=88)

print(d)
pickle.dumps(d)  # 将变量d进行序列化，成为bytes
print('\n序列化 = ',pickle.dumps(d))

# 序列化并保存在文件中
with open('D:\\test.txt','wb') as f:
    pickle.dump(d,f)

# 反序列化，从文件中取出
with open('D:\\test.txt','rb') as f:
    t = pickle.load(f)
print('\n反序列化 %s\n' % t)


########## python对象变成一个JSON
# ensure_ascii=True,保证所有传入的非ASCII的字符都被转义，如果为false，则保持原样输出
d = dict(name='Tony',age=19,address='xxx省xxx市')

js = json.dumps(d,ensure_ascii=False)
print('Python对象转为JSON = %s\n' % js)
#  ensure_ascii 默认值为True



########## JSON变成一个python对象
json_str ='{"name":"BOB","age":39,"address":"xxxx省"}'
cl = json.loads(json_str)
print("JSON转换为Python= %s\n" % cl)



##########  Python自定义类与JSON之间的转化
class Student(object):
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age


studentA = Student('tom',120,32)
# s = json.dumps(studentA)
# print(s)    # TypeError: Object of type 'Student' is not JSON serializable
# 因为自定义类无法直接转换为json，需要先转换为dict


#  使用default可选参数 ：就是把任意一个对象变成一个可序列为JSON的对象
#  将对象转换为dict
def studentToDict(stu):
    return {'name':stu.name,'age':stu.age,'score':stu.score}

s2 = json.dumps(studentA,default=studentToDict)   # 指定转换函数
print('自定义类转JSON= %s\n' % s2)


# 把任意class的实例变为dict：
#  通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
s3 = json.dumps(studentA,default = lambda obj: obj.__dict__)
print('任意类转换JSON = %s\n' % s3)

# json转类对象
def dictToStudent(d):
    return Student(d['name'],d['score'],d['age'])


json_str ='{"name":"BOB","age":39,"score":100}'
# loads()方法首先转换出一个dict对象
# object_hook函数负责把dict转换为Student实例：
j2C = json.loads(json_str,object_hook= dictToStudent)
print('json转类对象 ',j2C)


#  ************* slots 修饰的 class，不具有 dict 属性