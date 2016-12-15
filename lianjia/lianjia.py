# encoding=utf-8
import asyncio
import re
import time
import aiohttp 
import pymysql as mdb
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
 
# 插入数据
# async def insert_db(row):  
def insert_db(row):  
    global count  
    # print(row)
    try:
        con = mdb.connect('localhost', 'root','', 'lianjia'); 
        cur = con.cursor()     
        cur.execute('insert into house values(NULL,%s,%s,%s,%s,%s,%s)',row) 
        con.commit()  
        con.close()
        count += 1
        print('插入',count,'条数据')
    except Exception as e:
        print(e) 

# async def http_get(url):  
def http_get(url):  
    # res            = await aiohttp.request('GET', url) 
    # data           = await res.read() 
    data            = urllib2.urlopen(url).read()  
    data           = data.decode('utf-8') 
    re_ul          = r'<ul class="clinch-list">(.*?)</ul>'   
    re_li          = r'<li>(.*?)</li>'
    re_link        = r'<div class="pic-panel"><a href="(.*?)"'   
    re_name        = r'<div class="info-panel"><h2><a href=".*?" target="_blank">(.*?)</a></h2>'
    re_info        = r'<div class="other"><div class="con">(.*?)</div>' 
    re_price       = r'<div class="fl"><div class="div-cun">(.*?)</div>' 
    re_price_total = r'<div class="fr"><div class="div-cun">(.*?)</div>' 
 
    dr      = re.compile(r'<[^>]+>',re.S) 
    ul      = re.findall(re_ul, data,re.S)   
    li      = re.findall(re_li,ul[0],re.S)
    for i in range(len(li)):  
        row    = []
        link   = re.findall(re_link, li[i],re.S)[0]   
        name   = re.findall(re_name, li[i],re.S)[0]   
        info   = re.findall(re_info, li[i],re.S)[0]   
        prices = re.findall(re_price, li[i],re.S)
        total  = re.findall(re_price_total, li[i],re.S)
        date   = dr.sub('',prices[0]) 
        price  = dr.sub('',prices[1]) 
        price  = int(price.replace('元/平',''))
        total  = dr.sub('',total[0]) 
        total  = int(float(total.replace('万',''))*10000)
        row.append(link.encode('utf-8'))
        row.append(name.encode('utf-8'))
        row.append(info.encode('utf-8'))
        row.append(date.encode('utf-8'))
        row.append(price)
        row.append(total)   
        # await insert_db(row)
        insert_db(row)
    # print(url)
    # print(len(li))
    # print(items)
    # print(data)


def async_get(urls): 
    loop = asyncio.get_event_loop() 
    tasks = [http_get(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

print('抓取链家数据--协程')
count            = 0
page_pool = ThreadPool(30) 
urls = []
link = 'http://cd.lianjia.com/chengjiao/pg%s'
for x in range(1,2):
    url = link % (x)
    urls.append(url)
# print(urls) 
page_pool.map_async(http_get, (urls))
page_pool.close()
page_pool.join()   

# print('3个连接由一个线程通过coroutine并发完成')

# x = b'\xe9\x93\xbe\xe5\xae\xb6\xe7\xbd\x91\xe7\xad\xbe\xe7\xba\xa6'
# print(x.decode('utf-8'))
