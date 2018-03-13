#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('D:/aa.png')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

# 把缩放后的图像用jpeg格式保存:
im.save('D:/thumbnail.jpg', 'jpeg')


# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# 模糊
im2 = im.filter(ImageFilter.BLUR)
im2.save('D:/blur.jpg','jpeg')
im2.save('D:/blur.png','png')


# 绘图。生成字母验证码图片
# 随即字母
def rndChar():
    return chr(random.randint(65,90))

# 随即产生颜色(背景颜色)
def rndColor():
    return (random.randint(32,255),random.randint(16,255),random.randint(8,255))

# 随即产生颜色（字体颜色）
def rndFontColr():
    # return (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))
    return (random.randint(32,128),random.randint(32,128),random.randint(32,127))

width = 60 * 4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象
font = ImageFont.truetype('arial.ttf', 36)  # 使用Arial.ttf，报错，因为Windows 字体里是小写的
# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = rndColor())

# 输出文字：
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndFontColr())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('D:\code.jpg','jpeg')