# -*- coding: utf-8 -*-
import urllib2
import json  
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
import sys 
import time
import MySQLdb as mdb 
from getDataInMysql import insert_data

def getData():   
	try:         
		table = 'ltc_exchange_rate'
		url = 'https://www.okcoin.com/api/v1/exchange_rate.do' ; 
		data      = urllib2.urlopen(url).read() 
		json_dict = json.loads(data)       
		insert_data(table,json_dict.get('rate'))
		return json_dict.get('rate')
	except Exception, e:
		# print e
		getData() 
		
if __name__ == '__main__': 
	while True:   
		getData()
		time.sleep(5)
