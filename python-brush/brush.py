#-*- coding: UTF-8 -*-
import requests
import urllib
import sys
import math
import random 
import time    
from PIL import Image
import threading
from multiprocessing.dummy import Pool as ThreadPool


captcha_url = 'http://v5.10brandchina.com/api/captchar.vote.png.php?authType=5&rnd=40467543901241&id=54390&outb=0'
vote_url = 'http://v4.10brandchina.com/api/captcha.check.2.php?captcha=%s&rnd=40467543901241&authType=5&id=54390'
s           = requests.Session() 
 
r = s.get(captcha_url)
open('captcha.jpg','wb').write(r.content) 
im=Image.open('captcha.jpg')
im.show()
captcha=input('请输入验证码：') 
vote_url%(captcha)
res = s.get(vote_url).content
print(res) 
sys.exit()   
