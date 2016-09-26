# coding:utf-8
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
import random
import struct
import socket


def get_random_ip():
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

def test_proxy(ip): 
	print ip
	url = 'http://115.28.115.64/s/0eSGb-48475'
	# url = 'http://wp.zhongyulian.com/checkip.php' 
	# url = 'http://115.28.115.64/s/0CATs-c0793'
	client_ip = get_random_ip()
	# client_ip = ip.split(':')[0];
	# print client_ip
	# return 
	header = { 
	    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
	    "Accept-Language":"zh-CN,zh;q=0.8",
	    "Connection":"keep-alive",
	    "Host":"115.28.115.64",
	    "Upgrade-Insecure-Requests":"1",    
	    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"   ,
    	"CLIENT-IP":client_ip,
    	"X-FORWARDED-FOR":client_ip
    }
	proxy_support = urllib2.ProxyHandler({'http':  ip})
	opener        = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	req           = urllib2.Request(url)
	for key in header:
		req.add_header(key, header[key])
	html = urllib2.urlopen(req).read()
	print html

if __name__ == '__main__':

	# f = open("kuaidaili.txt")   
	# f = open("proxy.txt")  
	f = open("xici.txt")   
	line = f.readline()   
	proxy_list = []        
	while line:  
	    # print line,  
	    proxy_list.append(line)               
	    line = f.readline()  

	proxy_pool = ThreadPool(50) 
	proxy_pool.map_async(test_proxy, (proxy_list))
	proxy_pool.close()
	proxy_pool.join()
	f.close()   

