#!bin/python
#-*- coding: UTF-8 -*-
'''多万图库 spider  抓取囧图、gif'''

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
    begin_str = getBeginStr()
    print('http://tu.duowan.com/tu 从主页开始抓取')
    image_items = []
    url_index = 'http://tu.duowan.com/tu'
    prog_index = r'<em><a href="(.*)" target="_blank">(.*)</a>'
    data = urllib2.urlopen(url_index).read()
    print('获取网页成功') 
    data = data.decode('utf-8')
    index_items = re.findall(prog_index, data)  
    # pool = multiprocessing.Pool(5)
    for i,item in enumerate(index_items): 
        if begin_str in item[1]:
            break
        else:
            id = re.sub(r'\D', "", item[0])
            image_items.append(id)
            getImageUrl(id)
    #         pool.apply_async(getImageUrl, (id))
    # print(image_items)
    # pool.close()
    # pool.join() 
    clear_file()
    print ('*'*20+"抓取完成共耗时%.3fs" % (time.time() - _global_dict['start_time']))
    print ('*'*20+"共抓取%d个文件" %_global_dict['count']) 

def getImageUrl(id):
    url = 'http://tu.duowan.com/index.php?r=show/getByGallery/&gid='+id
    print('---从%s 抓取图片'%url)
    data = urllib2.urlopen(url).read()
    json_data = json.loads(data)
    # print(json_data['picInfo'][0]['source'])
    for item in json_data['picInfo']:
        if not item['source'].startswith('http:'):
            item['source']= 'http:'+item['source']
        download_image(item['source'],'./download/'+item['source'].split('/')[-1])

def download_image(image, store_file):
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

def clear_file():
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

                

            