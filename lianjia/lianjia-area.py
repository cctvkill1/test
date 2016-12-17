# -*- coding: utf-8 -*- 
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

def http_get(url):   
    data_id = url[0]
    url = url[1]
    # print(data_id) 
    data       = urllib2.urlopen(url).read()  
    data       = data.decode('utf-8') 
    re_link    = r'<div class="info fr">.*?<p>(.*?)</p>'
    link       = re.findall(re_link,data,re.S)[0]
    re_area    = r'<a .*?>(.*?)</a>'
    area_info       = re.findall(re_area,link,re.S)  
    xiaoqu     = area_info[0]
    area       = area_info[1]
    address    = area_info[2]
    update_sql = 'update house   set  xiaoqu ="'+xiaoqu+'" ,area ="'+area+'" ,address = "'+address+'" where  id ='  +str(data_id)+' ;'  
 
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
    global count   
    try:
        con     = mdb.connect('localhost', 'root','', 'lianjia',charset='utf8'); 
        cur     = con.cursor()     
        cur.execute(sql)   
        con.commit()  
        con.close() 
        count += 1  
        print('更新',count,'条数据')
    except Exception as e:
        print(e) 


print('抓取链家数据小区名字 地区 街道')
count            = 0
page_pool = ThreadPool(100)  
urls = getSqlData('select id,link from house WHERE house.area IS  null  ') 
# print(urls)  
page_pool.map_async(http_get, (urls))
page_pool.close()
page_pool.join()    