#!bin/python
#-*- coding: UTF-8 -*-


'''妹子图 spider
   URL: www.meizitu.com
   抓取网站所有图片
'''

import re
import string
# import urllib, urllib2
import os, sys
import multiprocessing 
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

def getPageA(page,store_dir):
    '''获取每个模块下的图片链接'''
    image_items = {}
    url_index = 'http://www.meizitu.com/a/list_1_%s.html' % page
    prog_index = r'<h3 class="tit"><a href="(.*)".*</a></h3>'

    data = urllib2.urlopen(url_index).read()
    print('get page done')

    data = data.decode('GBK')
    index_items = re.findall(prog_index, data)

    pool = multiprocessing.Pool(10)

    for index, item in enumerate(index_items):
        # image_items[index] = image_item
        pool.apply_async(getImageUrl(item,store_dir))      
    pool.close()
    pool.join()

    # return image_items

def getImageUrl(item,store_dir):  
    prog_pages = r'<img alt=.*src="(.*)" /><br />'
    pool = multiprocessing.Pool(20)  
    dataItem = urllib2.urlopen(item).read()
    print('get pic done')
    dataItem = dataItem.decode('GBK')
    image_item = re.findall(prog_pages,dataItem)
    print('re is done')
    for i, image in enumerate(image_item): 
        img = image.split('http://pic.meizitu.com/wp-content/uploads/');
        picUrl = img[1].replace("/", "-");
        print(picUrl)
        store_file = store_dir + str(picUrl) + '.jpg'
        pool.apply_async(downloadImage, (image, store_file))   
    pool.close()
    pool.join()
    
def downloadImage(image, store_file):
    if not os.path.exists(store_file):
        print('---pic start download---')
        urllib2.urlretrieve(image, store_file, call_back)
    else:
        print('pic is exists')

def BeginDownload(page):

    # pool = multiprocessing.Pool(24)
    store_dir = 'D:/test/meizitu/'

    if os.path.exists(store_dir):
        pass
    else:
        os.makedirs(store_dir)
        print('makedirs is done')

    image_items = getPageA(page,store_dir)
    print ('Page %s done!' % page)
    # for index in image_items:
    #     for i, image in enumerate(image_items[index]): 
    #         store_file = store_dir + str(index) + '-' + str(i) + '.jpg'
    #         pool.apply_async(downloadImage, (image, store_file))
    # pool.close()
    # pool.join()

def call_back(a, b, c):
    per = 100 * a * b / c
    if per < 100:
        sys.stdout.write('%.2f%%\r' % per)
        sys.stdout.flush()
    else:
        print ('---pic download finish!---')

if __name__ == '__main__':
 

    print ('''
             *************************************
             **       Welcome to use Spider     **
             **       Created on 2016-07-08     **
             **       Edit    on 2016-07-12     **
             **       @author: Jerry            **
             **       @editer: CCTV             **
             *************************************
          ''')

    page = '2'
    if '0' < page <= '88':
        BeginDownload(page)
        print ('All done!')
    elif page == 'all':
        for i in range(1, 89):
            BeginDownload(i)
        print ('All done!')
    else:
        print ('Error input!')
        sys.exit(-1)
