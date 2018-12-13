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
    _global_dict['begin_flag_file_name'] = 'begin_flag.txt'
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
        
def getBeginStr():    
    global _global_dict  
    f = open(_global_dict['begin_flag_file_name'], 'r+')
    begin_str = f.read()
    f.close()
    return begin_str

def setBeginStr(flag):    
    global _global_dict  
    f = open(_global_dict['begin_flag_file_name'], 'w+')
    f.write(flag)
    f.close()

def run(): 
    global _global_dict 
    begin_str = getBeginStr()
    print(begin_str)
    try: 
        print('http://tu.duowan.com/tu 从主页开始抓取')
        image_items = []
        url_index = 'http://tu.duowan.com/tu'
        prog_index = r'<em><a href="(.*)" target="_blank">(.*)</a>'
        data = urllib2.urlopen(url_index).read()
        data = data.decode('utf-8')
        index_items = re.findall(prog_index, data)  
        flag = ''
        # print('获取网页成功')
        # print(index_items)
        # pool = multiprocessing.Pool(5)
        for i,item in enumerate(index_items): 
            if i==0:
                flag = item[1]
            if i>=5:
                break
            elif begin_str and begin_str in item[1]:
                break
            else:
                id = re.sub(r'\D', "", item[0])
                image_items.append(id)
                getImageUrl(id) 
        #         pool.apply_async(getImageUrl, (id))
        # print(image_items)
        # pool.close()
        # pool.join()  
        setBeginStr(flag)
        clear_file()
        print ('*'*20+"抓取完成共耗时%.3fs" % (time.time() - _global_dict['start_time']))
        print ('*'*20+"共抓取%d个文件" % len(_global_dict['file_list'])) 
    except Exception as err:
        print(err)

def getImageUrl(id):
    global _global_dict   
    try:
        url = 'http://tu.duowan.com/index.php?r=show/getByGallery/&gid='+id
        # print('---从%s 抓取图片'%url)
        data = urllib2.urlopen(url).read()
        data = data.decode('utf-8')
        json_data = json.loads(data)
        # print(json_data['picInfo'][0]['source'])
        file_names = []
        for index,item in enumerate(json_data['picInfo']):
            if not item['source'].startswith('http:'):
                item['source']= 'http:'+item['source']
            file_name = _global_dict['duowan_path']+item['source'].split('/')[-1]
            _global_dict['file_list'].append({'title':item['add_intro'],'file_name':file_name})
            file_names.append([item['source'],file_name])
        for file_name in file_names:
            download_file(file_name[0],file_name[1])
    except Exception as err:
        print(err)

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
    # print('---清理完成')

if __name__ == '__main__': 
    _init()
    run()    

            