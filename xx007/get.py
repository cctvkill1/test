#-*- coding: UTF-8 -*-
import re
import string
import time 
import os
import sys
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
import pymysql as mdb
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# 插入数据
def insert_db(row):
    global count  
    # print(row)
    try:
        con = mdb.connect('localhost', 'root','123456', 'xx007'); 
        cur = con.cursor()     
        cur.execute('insert into users values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row) 
        con.commit()  
        con.close()
        count += 1
        print('插入',count,'条数据')
    except Exception as e:
        print(e) 
 
def get_html(url):
    try:
        data  = urllib2.urlopen(url).read()   
        data  = data.decode('GBK')
        return data
    except Exception as e:
        print(e) 

def get_board(boardid): 
    global url  
    global prog_board  
    global prog_board_total    
    board_url   = url+'index.asp?boardid=%s&page=%s' % (boardid,1)
    print("开始抓取板块页面",board_url)
    data_board  = get_html(board_url)
    board_total = re.findall(prog_board_total,data_board)
    board_page_total = int(board_total[0])
    items_board = re.findall(prog_board, data_board)   
    thread_child(items_board) 
    for b_page in range(2,board_page_total+1):
        board_url   = url+'index.asp?boardid=%s&page=%s' % (boardid,b_page)
        print("开始抓取板块页面",board_url)
        data_board  = get_html(board_url)
        items_board = re.findall(prog_board, data_board)   
        thread_child(items_board)

    print("----板块页面抓取完成",board_url)

def thread_child(items_board):
    threads = []
    page_size = 5
    length = len(items_board)
    if length>0: 
        num = int(length/page_size)
    for x in range(num):           
        thread = Thread(target=get_post_info, args=(items_board[x*page_size:(x+1)*page_size+1],))
        threads.append(thread)
        thread.start() 
    thread = Thread(target=get_post_info, args=(items_board[(x+1)*page_size:length-(x+1)*page_size-1],))
    threads.append(thread)
    thread.start()  
    for thread in threads:
        thread.join()   

def get_post_info(child): 
    global url  
    global prog_page  
    global prog_userinfo  

    try: 
        for c in child: 
            # #帖子页面只抓了第一页的
            page_url = url+c
            page_url = page_url.replace('&amp;','&')   
            print("开始抓取帖子页面",  page_url )
            data_page = get_html(page_url)
            if data_page:
                items_page = re.findall(prog_page, data_page,re.S)   
                userinfo = re.findall(prog_userinfo,data_page,re.S)
                for i in range(len(items_page)):          
                    items_page[i] = items_page[i].replace('<br/>','\n')  
                    dd = dr.sub('',items_page[i]) 
                    dd = dd.replace(' ','')   

                    row = []

                    data_re = re.findall(r'姓名[\s\:|\s\：](.*?)\n',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('') 
                    data_re = re.findall(r'手机[\s\:|\s\：](\d{11})',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'电话[\s\:|\s\：](.*?)&',dd) 
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')  
                    data_re = re.findall(r'微信[\s\:|\s\：](.*?)&',dd)  
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'支付宝[\s\:|\s\：](.*?)&',dd)  
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'地址[\s\:|\s\：](.*?)\n' ,dd) 
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'农行[\s\:|\s\：]([0-9]{19})',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'中行[\s\:|\s\：]([0-9]{19})',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'建行[\s\:|\s\：]([0-9]{19})',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'工行[\s\:|\s\：]([0-9]{19})',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'邮政[\s\:|\s\：]([0-9]{19})',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}',dd)
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('')
                    data_re = re.findall(r'QQ号[\s\:|\s\：](.*?)\n' ,dd) 
                    if len(data_re)>0:
                        data_re = str(data_re[0])
                        row.append(data_re.encode('utf-8')) 
                    else:
                        row.append('') 

                    userinfo_item = dr.sub('',userinfo[i])
                    userinfo_item = userinfo_item.replace(' ','')
                    userinfo_item = userinfo_item.replace('\r','') 
                    searchObj = re.search(r'交易等级：(.*?)\n', userinfo_item, re.S) 
                    if searchObj:
                        searchObj = str(searchObj.group(1)).encode('utf-8') 
                        row.append(searchObj) 
                    else:
                        row.append('') 
                    searchObj = re.search(r'信用积分：(.*?)\n', userinfo_item, re.S) 
                    if searchObj:
                        searchObj = str(searchObj.group(1)).encode('utf-8')
                        row.append(searchObj) 
                    else:
                        row.append('') 
                    searchObj = re.search(r'评分次数：(.*?)\n', userinfo_item, re.S) 
                    if searchObj:
                        searchObj = str(searchObj.group(1)).encode('utf-8')
                        row.append(searchObj) 
                    else:
                        row.append('') 
                    searchObj = re.search(r'发帖次数：(.*?)\n', userinfo_item, re.S) 
                    if searchObj:
                        searchObj = str(searchObj.group(1)).encode('utf-8')
                        row.append(searchObj) 
                    else:
                        row.append('') 
                    searchObj = re.search(r'发帖积分：(.*?)\n', userinfo_item, re.S) 
                    if searchObj:
                        searchObj = str(searchObj.group(1)).encode('utf-8')
                        row.append(searchObj) 
                    else:
                        row.append('') 
                    searchObj = re.search(r'注册日期：(.*?)\n', userinfo_item, re.S) 
                    if searchObj:
                        searchObj = str(searchObj.group(1)).encode('utf-8')
                        row.append(searchObj) 
                    else:
                        row.append('')    

                    insert_db(row) 
                print("=====帖子页面抓取完成",page_url)

    except Exception as e:
        print(e) 
if __name__ == '__main__':  
 

    start_time = time.time()  

    print ("开始抓取")

    url              = 'http://www2.xx007.cn/'
    prog             = r'<div><a href="index.asp\?boardid=(.*)">.*</a>' 
    prog_board       = r'<div class="listtitle"><a href=\"(.*?)\".*?</a>'
    prog_page        = r'<div style="width:85%;overflow-x: hidden;">(.*?)</div>'
    prog_userinfo    = r'<img style="margin:5px 0px 5px 0px;" src="skins/Default/star/.*?" /></div>(.*?)<div class="post">' 
    prog_board_total = r'<td class="tabletitle1">&nbsp;1/(.*?)页&nbsp;</td>'  
    dr               = re.compile(r'<[^>]+>',re.S) 
    count            = 0

    data = urllib2.urlopen(url).read()  
    print ("主页获取成功",url)
    data = data.decode('GBK')
    items = re.findall(prog, data)   

    page_pool = ThreadPool(int(len(items)/2))
    page_list = []
    for item in items:  
        page_list.append(item)
    page_pool.map_async(get_board, (page_list))
    page_pool.close()
    page_pool.join()   
    
    print ("【全部完成】共耗时%.2fs" % (time.time() - start_time)) 

 
