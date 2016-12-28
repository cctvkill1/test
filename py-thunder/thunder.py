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

async def open_thunder(downurl):
	os.execl(r"C:\Program Files (x86)\Thunder\Program\Thunder.exe" ,'-StartType:DesktopIcon '+downurl)

async def down_movie(movie):
	try:
		res            = await aiohttp.request('GET', movie['down_url']) 
		data           = await res.read()  
		soup       	   = BeautifulSoup(data,"html.parser")
		td       	   = soup.find('td',attrs={'bgcolor':"#ffffbb"})
		a 			   = td.find('a')
		url 		   = a.get('href')   
		if url.find("mp4") == -1 and url.find("mkv") == -1 and url.find("rmvb") == -1:
			print('连接不正确'+a.text+url)
		else: 
			print('开始下载'+a.text+url)
			QutoUrl = urllib.parse.quote(('AA'+url+'ZZ').encode('utf-8')) 
			downurl= 'thunder://'+(base64.b64encode(bytes(QutoUrl,'utf-8'))).decode('utf-8') 
			# linux才可以
			# pid = os.fork()
			# if pid == 0:
			# 	open_thunder(downurl) 
			# else:
			# 	pass
	except Exception as e: 
		print(e)
 

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
			print('准备下载 '+movie['name']+'【'+str(movie['rating_nums'])+'】 '+movie['down_url']) 
			await down_movie(movie)
		else:
			print('已经下载 '+movie['name']+'【'+str(movie['rating_nums'])+'】 ')



douban_baseurl = 'https://movie.douban.com/subject_search?search_text=' 
url            = 'http://www.dygang.com/'
filename 	   = 'down_movies.txt' 
# output = open(filename, 'w+')
# output.write('{"name":"精灵王座","rating_nums":"7.4"}')
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
for name in names:
	this_url       = name.get('href')	
	this_name      = name.text
	douban_url     = douban_baseurl+urllib.parse.quote(this_name)
	movie          = {}
	movie['url']      = douban_url
	movie['name']     = this_name
	movie['down_url'] = this_url
	movies.append(movie) 

loop = asyncio.get_event_loop()   
tasks = [rating_nums(movie) for movie in movies]
loop.run_until_complete(asyncio.wait(tasks))
loop.close() 