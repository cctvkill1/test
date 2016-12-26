# -*- coding: utf-8 -*-  
# import urllib.parse
# import base64
# import os

# url = 'ftp://7e:7e@d8.3edyy.com:161/【3E电影院www.eee4.cc】叶问2[DVD国语中字].rmvb' 
# print('准备下载'+url)
# QutoUrl = urllib.parse.quote(('AA'+url+'ZZ').encode('utf-8')) 
# downurl= 'thunder://'+(base64.b64encode(bytes(QutoUrl,'utf-8'))).decode('utf-8') 
# os.execl(r"C:\Program Files (x86)\Thunder\Program\Thunder.exe" ,'-StartType:DesktopIcon '+downurl)

# BeautifulSoup 例子
import urllib 
import urllib.request as request
import re
from bs4 import *
 
#url = 'http://zh.house.qq.com/'
url = 'http://www.0756fang.com/'
html = request.urlopen(url).read().decode('utf-8')
 
soup = BeautifulSoup(html,"html.parser")

# print (soup.find_all('a'))

links = soup.find_all('a')
hrefs = []
for link in links:
	href = link.get('href')
	# print(href)
	if href.endswith('.html'):
		hrefs.append(href)
print(hrefs)

# print(soup.head.meta['content'])#输出所得标签的‘’属性值
# print(soup.span.string);print(soup.span.text)#两个效果一样，返回标签的text
 
# #name属性是‘’的标签的<ResultSet>类，是一个由<Tag>组成的list
# print(soup.find_all(attrs={'name':'keywords'}))
# print(soup.find_all(class_='site_name'))#class属性是‘’的<Tag>的list,即<ResultSet>
# print(soup.find_all(class_='site_name'))#这是一个<Tag>
 
# print(soup.find(attrs={'name':'keywords'}))#name属性是‘’的标签的<Tag>类
# print(soup.find('meta',attrs={'name':'keywords'}))#name属性是‘’的meta标签的<Tag>类