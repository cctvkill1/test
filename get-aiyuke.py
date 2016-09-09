# encoding=utf-8
import urllib2
import urllib
import cookielib
import re
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
import sys
import codecs

def login(login_page, user, password): 
    try: 
        cj     = cookielib.CookieJar() 
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
        data   = urllib.urlencode({"username": user, "password": password, 'cookietime': 604800, 'submit': 1}) 
        opener.addheaders.append(('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'))
        opener.open(login_page, data)
        return opener
    except Exception, e:
        print 'error', str(e)

def get_child(child):
    global opener  
    global filename
    global childUrl
    prog_phone_input = re.compile('<input type=\"text\" name=\"mobile\" id=\"mobile\" value=\"(.*?)\".*?>',re.S)
    prog_phone_div   = re.compile('<div class=\"title\">手机号码：</div>.*?<div class=\"inputer\">.*?<div class=\"\">(.*?)</div>.*?</div>',re.S)
    prog_qq_input    = re.compile('<input type=\"text\" name=\"qq\" id=\"qq\" value=\"(.*?)\".*?>',re.S) 
    prog_qq_div      = re.compile('<div class=\"title\">QQ号码：</div>.*?<div class=\"inputer\">.*?<div class=\"\">(.*?)</div>.*?</div>',re.S)
    prog_sex         = re.compile('<input type=\"radio\" id=\"sex_boy\" name=\"clubsex\" value=\"0\"  checked=\"checked\".*?/>男',re.S)
        
    try: 
        f = open(filename,'a') 
        for i in child: 
            u = childUrl.format(i[1],i[0])  
            cdata      = opener.open(u).read()  

            phone      = ''
            qq         = ''
            sex        = ''
            phone_item = re.findall(prog_phone_input, cdata)
            if not phone_item:  
                phone_item = re.findall(prog_phone_div, cdata)
            if phone_item: 
                phone = phone_item[0] 
            if not phone:
                continue      
            qq_item = re.findall(prog_qq_input, cdata)
            if not qq_item: 
                qq_item = re.findall(prog_qq_div, cdata)
            if qq_item: 
                qq = qq_item[0]  

            sex_item = re.findall(prog_sex, cdata)
            if sex_item:
                sex = '男'
            else:
                sex = '女'
            dataString = i[2].strip()+','+phone.strip()+','+qq.strip()+','+i[3].strip()+','+sex
            f.write(dataString) 
            f.write("\n")  
        f.close()
        print 'write data over' 
    except Exception, e:
        print 'error', str(e)

def get_list(url):
    global opener  
    prog_index       = re.compile('<div class=\"item-list clearfix\" id=\"user-item-(.*?)\".*?data-cid=\"(.*?)\".*?data-username=\"(.*?)\".*?>.*?<div class=\"money\">(.*?)</div>',re.S)  
 
    try: 
        op     = opener.open(url)
        data   = op.read()  
        print 'get list-page ok'
        index_items = re.findall(prog_index, data)    
        threads = []
        page_size = 5
        length = len(index_items)
        num = int(length/page_size)
        for x in range(num):          
            # print index_items[x*page_size:(x+1)*page_size+1]
            thread = Thread(target=get_child, args=(index_items[x*page_size:(x+1)*page_size+1],))
            threads.append(thread)
            thread.start() 
        thread = Thread(target=get_child, args=(index_items[(x+1)*page_size:length-(x+1)*page_size-1],))
        threads.append(thread)
        thread.start()  
        for thread in threads:
            thread.join()   

      
    except Exception, e:
        print 'error', str(e)

if __name__ == '__main__':

    opener    = login("http://passport.tiyushe.com/?rc=SSO&ra=login&ajax=1",'cjjenter', 'cjj123456')
    url       = 'http://yuleymq.tiyushe.com/?c=clubmanage&a=member&cid=1415&page={0}' 
    childUrl  = 'http://yuleymq.tiyushe.com/?c=clubmanage&a=add_member&cid={0}&uid={1}'    
    filename  = 'getData.csv'
    totalPage = 50
    page_pool = ThreadPool(totalPage/2) 
    page_list = []
    for i in range(1, totalPage + 1):
        u = url.format(i)  
        page_list.append(u)
    page_pool.map_async(get_list, (page_list))
    page_pool.close()
    page_pool.join()

   