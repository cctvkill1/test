#-*- coding: UTF-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
# import mysql.connector 
import pymysql as mdb
import json
import sys
import math
import random
import time 
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
 
task_queue = queue.Queue();
def gettask():
    return task_queue;

def get_headers(_xsrf=''):
    # headers = {
    #         'Accept':'*/*',
    #         'Accept-Encoding':'gzip, deflate',
    #         'Accept-Language':'zh-CN,zh;q=0.8',
    #         'Connection':'keep-alive',
    #         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #         'Host':'www.zhihu.com',
    #         'Origin':'http://www.zhihu.com',
    #         'Referer':'http://www.zhihu.com/',
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    #         'X-Requested-With':'XMLHttpRequest'
    #         }
    headers = { 
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        # 'authorization':'oauth '+_xsrf,
        'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
        'Connection':'keep-alive',
        'Host':'www.zhihu.com',
        'Referer':'https://www.zhihu.com/people/ly941122/followers?page=2',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    return headers 

def get_mysql_con():
    con = mdb.connect('localhost', 'root','', 'zhihu');  
    return con

def get_user_json(next_url):
    global url
    # time.sleep(1)
    try: 
        print(next_url)
        res         = s.get(next_url) 
        data        = json.loads(res.text) 
        next        = data.get('paging').get('next')
        user_list   = data.get('data')
        next_spider = []
        for u in user_list: 
            if u.get('name') and u.get('avatar_url') and u.get('url_token'):
                avatarUrl = u.get('avatar_url') 
                avatarUrl = avatarUrl.replace('_is','_xl') 
                if avatarUrl!='https://pic1.zhimg.com/da8e974dc_is.jpg':
                    row = []            
                    row.append(u.get('name').encode('utf-8'))
                    row.append(avatarUrl.encode('utf-8'))
                    row.append(u.get('url_token').encode('utf-8'))  
                    r   = insert_data(row)
                    if r: 
                        next_spider.append(u.get('url_token')) 

        # if len(next_spider)>0:
        #     threads = []
        #     for item_spider in next_spider: 
        #         t = threading.Thread(target=spider(item_spider['url'],item_spider['token']))
        #         # t.setDaemon(True)
        #         t.start()
        #         threads.append(t)
        #     for thread in threads:
        #         thread.join()   

        if next and len(user_list)>0:
            get_user_json(next) 
 

    except Exception as e:
        print(e)  

def is_exist(sql):
    count   = cursor.execute(sql)   
    if count>0:
        return True
    return False

def insert_data(row):
    global count     
    try: 
        if row[2]:
            sql = 'select token  from users WHERE users.token = "'+row[2].decode('utf-8')+'"; '
            exist = is_exist(sql)
            if not exist:
                cursor.execute('insert into users values(NULL,%s,%s,%s)',row)
                count += 1
                cnx.commit()
                print('插入',count,'条数据')  
                return True
    except Exception as e:
        print(e)  
    return False

def spider(token):
    global url
    try:
        turl = url%(token)
        print(turl)
        response = s.get(turl)
        soup     = BeautifulSoup(response.text, "html.parser") 
        div      = soup.find(id='data')
        if div:
            json_data   = json.loads(div['data-state']) 
            users       = json_data.get('entities').get('users')
            next_spider = []
            for u in users:
                if users[u].get('name') and users[u].get('avatarUrl') and users[u].get('urlToken'):
                    avatarUrl = users[u].get('avatarUrl') 
                    if avatarUrl!='https://pic1.zhimg.com/da8e974dc_is.jpg':
                        avatarUrl = avatarUrl.replace('_is','_xl')  
                        row       = []
                        row.append(users[u].get('name').encode('utf-8'))
                        row.append(avatarUrl.encode('utf-8'))
                        row.append(users[u].get('urlToken').encode('utf-8')) 
                        r         = insert_data(row)
                        if r: 
                            next_spider.append(users[u].get('urlToken')) 

            next = json_data.get('people').get('followersByUser')
            next_url = next[token].get('next')
            if next_url: 
                get_user_json(next_url)  

            if len(next_spider)>0: 
                for item_spider in next_spider: 
                    task.put(item_spider); 
             
    except Exception as e:
        print(e)  

if __name__ == '__main__':
    print('知乎关注用户爬虫开始')
    count       = 0
    signin_url  = 'http://www.zhihu.com/#signin'
    login_url   = 'http://www.zhihu.com/login/email'
    captcha_url = 'https://www.zhihu.com/captcha.gif'
    gz_url      = 'https://www.zhihu.com/node/ProfileFolloweesListV2'
    url         = 'https://www.zhihu.com/people/%s/followers'
    token       = 'zhang-jia-wei'
    s           = requests.Session() 
    headers     = get_headers()
    s.headers   = headers


    cnx = get_mysql_con()
    cursor = cnx.cursor()    
     
    freeze_support()
    BaseManager.register('get_task',callable = gettask); 
    manager = BaseManager(address = ('127.0.0.1',5000),authkey = b'123'); 
    manager.start();
    try: 
        task = manager.get_task();  
    except Exception as e:
        print('Manager error:',e);
    finally: 
        time.sleep(1);
        manager.shutdown();
            
    spider(token)

    cursor.close()
    cnx.close()