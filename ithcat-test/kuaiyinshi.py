#!bin/python
#-*- coding: UTF-8 -*-
'''快音视爬虫'''

import re
import string
import json
import time
import os
import sys
import multiprocessing
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
 
import uuid




def _init():
    global _global_dict 
    _global_dict = {}
    _global_dict['count'] = 0 
    _global_dict['start_time'] = time.time()  
  

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
        
def getBeginStr():    
    f = open('begin_flag.txt', 'r')
    begin_str = f.read().split('：')[0]
    return begin_str
    

def run():
    global _global_dict    
    test = 'http://api.amemv.com/aweme/v1/playwm/?video_id=v0300fff0000bg66gp782ijmppllk290&line=0&ratio=720p&media_type=4&vr_type=0&test_cdn=None&improve_bitrate=0'
    item = {}
    item['video_url'] = test
    print('开始下载视频  %s'%item['video_url'])
    req = urllib2.Request(item['video_url'])
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    req.add_header("GET",item['video_url'])
    req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8") 
    req.add_header("Host","api.amemv.com") 
    req.add_header("Upgrade-Insecure-Requests","1")
    data = urllib2.urlopen(item['video_url']).read()
    print(data)
    # url = 'http://kuaiyinshi.com/api/hot/videos/?source=dou-yin&page=1&st=week'
    # print('---获取快音视API:%s '%url)
    # data = urllib2.urlopen(url).read()
    # json_data = json.loads(data)
    # # print(json_data['picInfo'][0]['source'])
    # for item in json_data['data']:
    #     print(item['desc']+"  "+item['video_url'])
    #     if not item['video_url'].startswith('http:'):
    #         item['video_url']= 'http:'+item['video_url']
    #     print('开始下载视频  %s'%item['video_url'])
    #     req = urllib2.Request(item['video_url'])
    #     req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    #     req.add_header("GET",item['video_url'])
    #     req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8") 
    #     req.add_header("Host","api.amemv.com") 
    #     req.add_header("Upgrade-Insecure-Requests","1")
    #     data = urllib2.urlopen(item['video_url']).read()
    #     print(data)
    #     # download_file(item['video_url'],'./download/'+str(uuid.uuid4())+'.mp4')
    #     break
    # print ('*'*20+"抓取完成共耗时%.3fs" % (time.time() - _global_dict['start_time']))
    # print ('*'*20+"共抓取%d个文件" %_global_dict['count']) 

def download_file(image, store_file):
    if not os.path.exists(store_file):
        print('----%s start download----'%image)
        urllib2.urlretrieve(image, store_file, call_back)
    else:
        print('file is exists')
 

def call_back(a, b, c):
    global _global_dict
    per = 100 * a * b / c
    if per < 100:
        sys.stdout.write('%.2f%%\r' % per)
        sys.stdout.flush()
    else:
        print ('----file download finish!----')        
        _global_dict['count'] += 1

def clearfile():
    global _global_dict
    rootdir = './download/'
    types = ['.jpg','.jpeg','.gif','.mp4'] 
    file_list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(file_list)):
        path = os.path.join(rootdir,file_list[i])
        if os.path.isfile(path):
            filename,filetype = os.path.splitext(path) 
            t = os.path.getctime(path)
            fsize = os.path.getsize(path)
            fsize = round(fsize/float(1024*1024) ,2)
            if filetype not in types or fsize>6:
                os.remove(path)
                print(filename+filetype+'   '+str(fsize))
            elif t<_global_dict['start_time']-3600:
                os.remove(path)



if __name__ == '__main__': 
    _init()
    run()    
# TODO get http://kuaiyinshi.com/api/hot/videos/?source=dou-yin&page=1&st=week&callback=showData&_=1544540194280
# code = 200 然后 data[0]['desc']和['video_url']

                

            