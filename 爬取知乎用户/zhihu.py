# #encoding=utf-8
# try:
#     import urllib.request as urllib2
# except ImportError:
#     import urllib2 
# import http.cookiejar as cookielib
# import urllib  
# import sys 
# import re

# try: 
#     cookie = cookielib.CookieJar()
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#     postdata = urllib.parse.urlencode({
#                 'email':'321@qq.com',
#                 'remember_me':'true',
#                 'password':'321'
#             })
#     postdata = postdata.encode('utf-8') 
#     loginUrl = 'https://www.zhihu.com/login/email' 
#     result = opener.open(loginUrl,postdata) 
#     # testUrl  = 'https://www.zhihu.com/people/zhang-jia-wei/followers?page=3'
#     testUrl = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=20&limit=10'
 
#     result = opener.open(testUrl)
#     # print(result)
#     data = result.read() 
#     data = data.decode("UTF-8");
#     # print (data)

#     re_img       = r'<img class="Avatar .*?src="(.*?)"'
#     img_items = re.findall(re_img, data)   
#     print(img_items)
#     print(len(img_items) ) 

# except Exception as e:
#     print (e)


#-*- coding: UTF-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
# import mysql.connector
import json
import sys
import math
import random
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2 

def get_opener(login_page, email, password): 
    try: 
        html    = urllib2.urlopen(signin_url).read()
        soup    = BeautifulSoup(html,'html.parser')
        _xsrf   = soup.find('input',{'type':'hidden','name':'_xsrf'})['value'] 
        r       = urllib2.urlopen(captcha_url).read()
        open('captcha.gif','wb').write(r)
        captcha = input('请输入验证码：')
        data    = get_post_data(email,password,captcha,_xsrf)
        headers = get_headers()  
        cj      = cookielib.CookieJar() 
        opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
        opener.addheaders = headers
        opener.open(login_page, data)
        return opener
    except Exception, e:
        print 'error', str(e)
def get_post_data(email,password,captcha,_xsrf):
    data = {
            '_xsrf':_xsrf,
            'password':password,
            'remember_me':'true',
            'email':email,
            'captcha':captcha 
            }
    return data
    
def get_headers():
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
    headers = [
            ('Accept','*/*'),
            ('Accept-Encoding':'gzip, deflate'),
            ('Accept-Language':'zh-CN,zh;q=0.8'),
            ('Connection':'keep-alive'),
            ('Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'),
            ('Host':'www.zhihu.com'),
            ('Origin':'http://www.zhihu.com'),
            ('Referer':'http://www.zhihu.com/'),
            ('User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'),
            ('X-Requested-With':'XMLHttpRequest')
            ]
    return headers

def get_config():
    config = {
            'host':'localhost',
            'user':'root',
            'password':'sql_password',
            'port':3306 ,
            'database':'zhihu'
            }
    return config

# def get_mysql_cnx():
#     config = get_config()
#     cnx = mysql.connector.connect(**config)
#     return cnx

def get_user_hash(text):
    soup = BeautifulSoup(text, 'html.parser')
    json_data = soup.find('script',{'class':'json-inline', 'data-name':'current_people'}).get_text().split('"')
    return json_data[7]
    
def get_XHR_data(offset,_xsrf,user_hash):
    data = {
            'method':'next',
            'params':'{"offset":%d,"order_by":"created","hash_id":"%s"}'%(offset,user_hash),
            '_xsrf':_xsrf
            }
    return data

def get_gzcnt(soup):
    res = soup.find('div',{'class':'zm-profile-side-following zg-clear'})
    return int(res.text.split()[1])

def spider(turl):
    global tot_count
    global url
    if(tot_count>=100000):
        return
    try:
        response = s.get(turl)
    except Exception as e:
        return 
    soup = BeautifulSoup(response.text, "html.parser")
    user_hash = get_user_hash(response.text)
    gzcnt = get_gzcnt(soup)
    next_id = []
    for i in range(math.floor(gzcnt/20)+1):
        cnt = i*20
        if(cnt>gzcnt):
            cnt=gzcnt
        elif(gzcnt==(i-1)*20):
            break
        try:
            tmp_json = json.loads(s.post(gz_url,get_XHR_data(i*20,_xsrf,user_hash)).text)
        except Exception as e:
            continue
        ts = BeautifulSoup(str(tmp_json['msg']), "html.parser")
        tres = ts.find_all('div',{'class':'zm-list-content-medium'})
        for x in tres:
            name = x.find('a').get_text()
            data = x.find_all('a',{'class':'zg-link-gray-normal'})
            id = x.find('a')['data-tip'][4:]
            info=[]
            for j in range(4):
                tmpsoup = BeautifulSoup(str(data[j]), "html.parser");
                info.append(tmpsoup.get_text().split(' ')[0])
            print(name)
            print(info)
            # insert_sql = "insert into user1(id,name,follower,ask,answer,zt) values (\'%s\',\'%s\',%s,%s,%s,%s)"%(id,name,info[0],info[1],info[2],info[3])
            # try:
            #     cursor.execute(insert_sql)
            #     tot_count = tot_count + 1
            #     cnx.commit()
            #     if(tot_count>=100000):
            #         return
            #     print('%d 用户[%s]信息添加完毕'%(tot_count,id))
            #     next_id.append(id)
            # except Exception as e:
            #     print('用户[%s]信息添加失败'%(id))    
        if(tot_count>=10):
            return    
    for x in next_id:
        spider(url%(x))




tot_count = 0

signin_url='http://www.zhihu.com/#signin'
login_url='http://www.zhihu.com/login/email'
captcha_url = 'https://www.zhihu.com/captcha.gif'
gz_url = 'https://www.zhihu.com/node/ProfileFolloweesListV2'
url = 'https://www.zhihu.com/people/zhang-jia-wei/followees' 
email = '1097422313@qq.com'
password = 'mvp511747'
opener    = get_opener(login_url,email, password)

# s = requests.Session()
# response = s.get(signin_url)
html = urllib2.urlopen(signin_url).read()
soup = BeautifulSoup(html,'html.parser')
_xsrf = soup.find('input',{'type':'hidden','name':'_xsrf'})['value']
# r = s.get(captcha_url, params = {'r':random.random(),'type':'login'}) 
r = urllib2.urlopen(captcha_url).read()
open('captcha.gif','wb').write(r)
captcha=input('请输入验证码：')
data = get_post_data(_xsrf,captcha)
headers = get_headers()
res = s.post(login_url,data,headers)
json_data = json.loads(res.text)
print(json_data['msg'])
if(json_data['r']!=0):
    sys.exit()   

# cnx = get_mysql_cnx()
# cursor = cnx.cursor()    

spider(url%('ly941122'))

# cursor.close()
# cnx.close()