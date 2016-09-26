# -*- coding:utf8 -*-
import requests
import re
import time
import random
import struct
import socket
import urllib2  

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from BeautifulSoup import BeautifulSoup


def get_haoip(): 
    of = open('haoip.txt', 'w') 
    for i in range(1,2):
        url = 'http://www.haoip.cc/' #+ str(i)
        print "正在采集"+url
        html = requests.get(url).text
        bs = BeautifulSoup(html) 
        table = bs.findAll('table',{"class":"proxy_table"}) 
        for x in table:    
            tr = x.findAll('tr')
            for y in tr:
                td = y.findAll('td') 
                if len(td)!=7:
                    continue 
                if td[4].string == u'高匿': 
                    of.write(td[0].string.strip()+':'+td[1].string.strip())
                    of.write('\n') 
    of.closed

def get_kuaidaili(): 
    of = open('kuaidaili.txt', 'w') 
    for i in range(1,5):
        url = 'http://www.kuaidaili.com/proxylist/' + str(i)
        print "正在采集"+url
        html = requests.get(url).text
        bs = BeautifulSoup(html) 
        table = bs.find('table',{"class":"table table-bordered table-striped  table-index"})  
        tr = table.findAll('tr')        
        for y in tr[1:]:
            td = y.findAll('td')  
            if td[2].string == u'高匿名':  
                of.write(td[0].string.strip()+':'+td[1].string.strip())
                of.write('\n') 
    of.closed

def get_xici():  
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    f = open('xici.txt', 'w') 
    for i in range(1,3):
        url = 'http://www.xicidaili.com/nn/' + str(i)
        print "正在采集"+url
        req = urllib2.Request(url,headers=header)
        res = urllib2.urlopen(req).read()

        soup = BeautifulSoup(res.encode('utf-8'))
        ips = soup.findAll('tr')

        for x in range(1,len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip_temp = tds[1].contents[0]+':'+tds[2].contents[0]+"\n"
            # print tds[1].contents[0]+':'+tds[2].contents[0]
            f.write(ip_temp)
    f.closed 


def __get_random_ip():
    RANDOM_IP_POOL=['192.168.10.222/0']
    str_ip = RANDOM_IP_POOL[random.randint(0,len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I',socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | ( 1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

if __name__ == '__main__':
    # get_haoip()
    # get_kuaidaili()
    get_xici()

    # print __get_random_ip()