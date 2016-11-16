#-*- coding: UTF-8 -*-
import re
import string
import time 
import os
import sys
import multiprocessing 
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# 登录（验证码识别）
def login(login_page, user, password):  
    # from pytesser import *
    # im = Image.open('fonts_test.png')
    # text = image_to_string(im)
    # print "Using image_to_string(): "
    # print text
    # text = image_file_to_string('fonts_test.png', graceful_errors=True)
    # print "Using image_file_to_string():"
    # print text
    cj     = cookielib.CookieJar() 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
    data   = urllib.urlencode({"username": user, "password": password, 'cookietime': 604800, 'submit': 1}) 
    opener.addheaders.append(('User-agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'))
    opener.open(login_page, data)
    return opener 

 
if __name__ == '__main__':

    start_time = time.time() 

    # page = '5'
    # if '0' < page <= '88':
    #     BeginDownload(page)
    #     print ('All done!')
    # elif page == 'all':
    #     for i in range(1, 89):
    #         BeginDownload(i)
    #         print ('Page %s done!' % i)
    #     print ('All done!')

    # print (count, "张图片")


    print ("开始抓取")

    url='http://www.xx007.cn/'
    prog = r'<div><a href="index.asp\?boardid=(.*)">.*</a>' 
    prog_board = r'<div class="listtitle"><a href=\"(.*?)\".*?</a>'
    prog_page  = r'<div style="width:85%;overflow-x: hidden;">(.*?)</div>'
    prog_board_total  = r'<td class="tabletitle1">&nbsp;1/(.*?)页&nbsp;</td>' 

    data = urllib2.urlopen(url).read()  
    print ("主页获取成功",url)
    data = data.decode('GBK')
    items = re.findall(prog, data)  
    # print(len(items))  #77板块
    for item in items: 
        board_url = url+'index.asp?boardid=%s&page=%s' % (item,1)
        print("开始抓取板块页面",board_url)
        data_board = urllib2.urlopen(board_url).read()   
        data_board = data_board.decode('GBK')
        board_total = re.findall(prog_board_total,data_board)
        # print(board_total)
        items_board = re.findall(prog_board, data_board)   
        for item_board in items_board: 
            #帖子页面只抓了第一页的
            page_url = url+'/%s' % item_board
            page_url = page_url.replace('&amp;','&')  
            print("开始抓取帖子页面",  page_url )
            data_page = urllib2.urlopen(page_url).read()   
            data_page = data_page.decode('GBK')
            # print(data_page) 
            items_page = re.findall(prog_page, data_page,re.S)  
            # print(items_page) 
            for item_page in items_page: 
                # print(item_page)  
                item_page = item_page.replace('<br/>','\n') 
                item_page = item_page.replace(' ','')  
                dr = re.compile(r'<[^>]+>',re.S)
                dd = dr.sub('',item_page)
                print(dd)
                get_bank_card = r'姓名：(.*?)\n' 
                bank_card = re.findall(get_bank_card,dd)[0]  
                print(bank_card) 
                get_phone = r'手机：(\d{11})' 
                phone = re.findall(get_phone,dd)[0] 
                print(phone)
                get_bank_card = r'农行：([0-9]{19})' 
                bank_card = re.findall(get_bank_card,dd)[0]  
                print(bank_card)
                get_bank_card = r'工行：([0-9]{19})' 
                bank_card = re.findall(get_bank_card,dd)[0]  
                print(bank_card)
                get_bank_card = r'地址：(.*?)\n' 
                bank_card = re.findall(get_bank_card,dd)[0]  
                print(bank_card)  
                # get_bank_card = r'QQ号：(.*?)\n' 
                # bank_card = re.findall(get_bank_card,dd)[0]  
                # print(bank_card) 
                
                #支付宝
                # 电话：0431-88761800 

            break
        break
    print ("共耗时%.2fs" % (time.time() - start_time)) 

 
