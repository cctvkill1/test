# -*- coding: utf-8 -*-  
import urllib 
import urllib.request as request
import re
import sys
from bs4 import *
import asyncio
import aiohttp
import urllib.parse
import base64
import os
# import json
# from multiprocessing.dummy import Pool as ThreadPool    
# import win32clipboard as w    
# import win32con  
# import win32api  
 

def getText():#读取剪切板  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_TEXT)  
    w.CloseClipboard()  
    return d  

def setText(aString):#写入剪切板  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_TEXT, aString)  
    w.CloseClipboard()   

def open_thunder(downurl=''):
	os.execl(r"C:\Program Files (x86)\Thunder\Program\Thunder.exe" ,'-StartType:DesktopIcon '+downurl)

async def down_movie(movie):
	try:
		res            = await aiohttp.request('GET', movie['down_page']) 
		data           = await res.read()  
		soup       	   = BeautifulSoup(data,"html.parser")
		tds       	   = soup.find_all('td',attrs={'bgcolor':"#ffffbb"})
		for td in tds: 
			a 			   = td.find('a')
			if a:
				url 		   = a.get('href')   
				if url.find("mp4") == -1 and url.find("mkv") == -1 and url.find("rmvb") == -1:
					pass
				else:  
					print('---准备下载 '+movie['name']+'【'+str(movie['rating_nums'])+'】 '+movie['down_page']) 
					QutoUrl = urllib.parse.quote(('AA'+url+'ZZ').encode('utf-8')) 
					downurl= 'thunder://'+(base64.b64encode(bytes(QutoUrl,'utf-8'))).decode('utf-8')  
					movie['downurl'] = downurl
					down_movies.append(movie)
					return
	except Exception as e: 
		print('error: '+movie['name']+' '+movie['down_page'])
 

async def rating_nums(movie): 
	res            = await aiohttp.request('GET', movie['url']) 
	data           = await res.read()  
	soup       	   = BeautifulSoup(data,"html.parser")
	span       	   = soup.find('span',attrs={'class':"rating_nums"})
	movie['rating_nums'] = float(span.text)
	if movie['rating_nums']>=7: 
		flag = False
		for m in movie_list:
			if m['name']==movie['name']:
				flag = True
				break
		if not flag:
			await down_movie(movie)
		else:
			print('已经下载 '+movie['name']+'【'+str(movie['rating_nums'])+'】 ')



douban_baseurl = 'https://movie.douban.com/subject_search?search_text=' 
url            = 'http://www.dygang.com/'
filename 	   = 'down_movies.txt' 
f = open(filename,"r")
movie_lines = f.readlines()
movie_list = []
for line in movie_lines:
	# print(line)
	movie = eval(line)
	movie_list.append(movie)


html           = request.urlopen(url).read()
soup           = BeautifulSoup(html,"html.parser")
div            = soup.find(id="tab1_div_0")
names          = div.find_all(class_ = 'c2')
movies 		   = []
down_movies    = [] 
for name in names:
	this_url       = name.get('href')	
	this_name      = name.text
	douban_url     = douban_baseurl+urllib.parse.quote(this_name)
	movie          = {}
	movie['url']      = douban_url
	movie['name']     = this_name
	movie['down_page'] = this_url
	movies.append(movie) 

loop = asyncio.get_event_loop()   
tasks = [rating_nums(movie) for movie in movies]
loop.run_until_complete(asyncio.wait(tasks))
loop.close() 
# print(down_movies)
copy = ''
if len(down_movies)>0:
	output = open(filename, 'a+')
	for m in down_movies:
		# print(json.loads(m))
		copy += m['downurl']+'\n'
		output.write('{"name":"'+m['name']+'","rating_nums":"'+str(m['rating_nums'])+'"}\n')
	output.close()
# linux才可以fork分支
# pid = os.fork()
# if pid == 0:
# 	open_thunder(downurl) 
# else:
# 	pass
# 多进程也不行 excel调用迅雷只有第一次才有用
# page_pool = ThreadPool(10) 
# page_list = [] 
# page_pool.map_async(open_thunder, (down_movies))
# page_pool.close()
# page_pool.join()
# 复制到剪切板再打开迅雷(pywin32库暂时没有python3.5版本的)
if copy:
	print('**************************请手动复制,然后打开迅雷**************************')
	print(copy)
	# setText(copy)
	open_thunder()

print('**************************over**************************')