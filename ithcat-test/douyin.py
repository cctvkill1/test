#!bin/python
#-*- coding: UTF-8 -*-
'''快音视爬虫 抓抖音周热'''

import re
import string
import json
import time
import os
import sys
import requests
import multiprocessing
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def _init():
    global _global_dict 
    _global_dict = {}
    _global_dict['count'] = 0 
    _global_dict['start_time'] = time.time()
    _global_dict['duowan_path'] = './download/'
    _global_dict['file_list'] = []
    if not os.path.exists(_global_dict['duowan_path']):
        os.mkdir(_global_dict['duowan_path'])
  

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue

def run():
    global _global_dict
    try:
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        file_names = []
        for num in range(1,3):
            url = 'http://kuaiyinshi.com/api/hot/videos/?source=dou-yin&page=%s&st=week'%num
            print('---获取快音视API:%s '%url)
            data = urllib2.urlopen(url).read()
            # data = data.decode('utf-8')
            json_data = json.loads(data) 
            for index,item in enumerate(json_data['data']):
                if not item['video_url'].startswith('http:'):
                    item['video_url']= 'http:'+item['video_url']
                # print(str(index+1+(num-1)*20)+"  "+item['desc']+"  "+item['video_url']) 
                # 这里有个问题 抖音的视频源地址是amemv.com的 然后302到西瓜视频源 利用requests返回Location解决问题 一定要User-Agent
                headers = {'Accept':     'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch, br',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Connection': 'keep-alive',
                    'Host': 'api.amemv.com',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        
                html = requests.get(item['video_url'], headers=headers, allow_redirects=False)
                mp4url = html.headers['Location'] 
                file_name = _global_dict['duowan_path']+date+' '+str(index+1+(num-1)*20)+'.mp4'
                _global_dict['file_list'].append({'title':item['desc'],'file_name':file_name})
                file_names.append([mp4url,file_name])
        for file_name in file_names:
            download_file(file_name[0],file_name[1])
        clear_file()

    except Exception as err:
        print(err)

    print ('*'*20+"抓取完成共耗时%.3fs" % (time.time() - _global_dict['start_time']))
    print ('*'*20+"共抓取%d个文件" % len(_global_dict['file_list'])) 

def download_file(image, store_file):
    try:
        if not os.path.exists(store_file):
            # print('----%s start download----'%image)
            urllib2.urlretrieve(image, store_file, call_back)
        else:
            # print('file is exists')
    except Exception as err:
        print(err)

def call_back(a, b, c):
    global _global_dict
    per = 100 * a * b / c
    if per < 100:
        sys.stdout.write('%.2f%%\r' % per)
        sys.stdout.flush()
    else:
        # print ('----file download finish!----')        
        _global_dict['count'] += 1

# 清理老文件 大文件（发gif图不能大于6M 发视频不能大于10M）
def clear_file():
    global _global_dict
    for i,item in enumerate(_global_dict['file_list']):
        path = item['file_name']
        t = os.path.getctime(path)
        fsize = os.path.getsize(path)
        fsize = round(fsize/float(1024*1024) ,2)
        if fsize<6 and t>_global_dict['start_time']-80000:
            pass
        else:
            # print('删除文件 %s'%path)
            os.remove(path)
            del _global_dict['file_list'][i]
    # print(_global_dict['file_list'])

if __name__ == '__main__': 
    _init()
    run()   
                

            