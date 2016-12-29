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
import threading


def get_data(_xsrf,captcha):
    data = {
            '_xsrf':_xsrf,
            'password':'xxx',
            'remember_me':'true',
            'email':'xxx@qq.com',
            'captcha':captcha
            }
    return data
    
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
                        item_spider = {'url':url%(u.get('url_token')),'token':u.get('url_token')}
                        next_spider.append(item_spider) 

        if len(next_spider)>0:
            for item_spider in next_spider: 
                t = threading.Thread(target=spider(item_spider['url'],item_spider['token']))
                t.setDaemon(True)
                t.start()
                t.join(30)

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

def spider(turl,token):
    global url
    try:
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
                            item_spider = {'url':url%(users[u].get('urlToken')),'token':users[u].get('urlToken')}
                            next_spider.append(item_spider) 

            next = json_data.get('people').get('followersByUser')
            next_url = next[token].get('next')
            if next_url: 
                get_user_json(next_url)  

            if len(next_spider)>0:
                for item_spider in next_spider: 
                    t = threading.Thread(target=spider(item_spider['url'],item_spider['token']))
                    t.setDaemon(True)
                    t.start()
                    t.join(30)
             
    except Exception as e:
        print(e)  


count       = 0
signin_url  = 'http://www.zhihu.com/#signin'
login_url   = 'http://www.zhihu.com/login/email'
captcha_url = 'https://www.zhihu.com/captcha.gif'
gz_url      = 'https://www.zhihu.com/node/ProfileFolloweesListV2'
url         = 'https://www.zhihu.com/people/%s/followers'
token        = 'zhang-jia-wei'
s           = requests.Session() 
headers     = get_headers()
s.headers   = headers

# 根本不需要登录 擦擦擦浪费时间 
# response = s.get(signin_url)
# soup = BeautifulSoup(response.text,'html.parser')
# _xsrf = soup.find('input',{'type':'hidden','name':'_xsrf'})['value']
# print(_xsrf)
# headers = get_headers(_xsrf)
# print(headers)
# sys.exit()
# s.headers = headers
# r = s.get(captcha_url, params = {'r':random.random(),'type':'login'})
# open('captcha.gif','wb').write(r.content)
# captcha=input('请输入验证码：')
# data = get_data(_xsrf,captcha)
# res = s.post(login_url,data,headers)

# json_data = json.loads(res.text)
# print(json_data['msg'])
# if(json_data['r']!=0):
#     sys.exit()   

cnx = get_mysql_con()
cursor = cnx.cursor()    

spider(url%(token),token)

cursor.close()
cnx.close()