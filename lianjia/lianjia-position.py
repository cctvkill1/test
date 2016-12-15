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
    data_id = url[0]
    url = url[1]
    print(data_id)
    # res            = await aiohttp.request('GET', url) 
    # data           = await res.read() 
    data            = urllib2.urlopen(url).read()  
    data            = data.decode('utf-8') 
    re_link         = r'<div class="info fr">.*?<a href="(.*?)" class="name"'    
    link            = re.findall(re_link,data,re.S)[0]
    # print(link)
    link = 'http://cd.lianjia.com/'+link
    data            = urllib2.urlopen(link).read()  
    data            = data.decode('utf-8') 
    re_pos          = r'resblockPosition:\'(.*?)\''   
    position        = re.findall(re_pos,data,re.S)[0] 
    coordinate = position.split(',')
    lng = coordinate[0]
    lat = coordinate[1]
    update_sql = 'update house      set  lng ="'+lng+'" ,lat = "'+lat+'" where  id ='  +str(data_id)+' ;'    
    print(update_sql)
    commitSqlData(update_sql)
 

def getSqlData(sql):  
    con     = mdb.connect('localhost', 'root','', 'lianjia'); 
    cur     = con.cursor()     
    count   = cur.execute(sql)  
    results = cur.fetchall()    
    con.close()
    return results

def commitSqlData(sql):  
    con     = mdb.connect('localhost', 'root','', 'lianjia'); 
    cur     = con.cursor()     
    cur.execute(sql)   
    con.commit()  
    con.close() 
    print('更新成功')


print('抓取链家数据小区坐标--协程')
count            = 0
page_pool = ThreadPool(100)  
urls = getSqlData('select id,link from house WHERE house.lng IS  null ') 
# print(urls)  
page_pool.map_async(http_get, (urls))
page_pool.close()
page_pool.join()   

# print('3个连接由一个线程通过coroutine并发完成')

# x = b'\xe9\x93\xbe\xe5\xae\xb6\xe7\xbd\x91\xe7\xad\xbe\xe7\xba\xa6'
# print(x.decode('utf-8'))
