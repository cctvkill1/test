# #encoding=utf-8
from PIL import Image
import os

# print (os.getcwd())
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
im.show()