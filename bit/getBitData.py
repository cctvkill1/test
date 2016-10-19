
# -*- coding: utf-8 -*-
import urllib2
import json  
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
import sys 
import time
import MySQLdb as mdb
  
def getBTCCNY(i=0): 
    if i == 0: 
        table = 'btc_cny'
        url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny' ;
    else: 
        table = 'ltc_cny'
        url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny';
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    row = [float(json_dict.get('ticker').get('last')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('ticker').get('last') 

def getExchange_rate(i=0):
    if i == 0: 
        table = 'btc_exchange_rate'
        url = 'https://www.okcoin.com/api/v1/exchange_rate.do' ;
    else: 
        table = 'ltc_exchange_rate'
        url = 'https://www.okcoin.com/api/v1/exchange_rate.do';
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)        
    row = [float(json_dict.get('rate')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('rate')

def getBTCUSD(i=0):
    if i == 0: 
        table = 'btc_usd'
        url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd' ;
    else: 
        table = 'ltc_usd'
        url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)       
    row = [float(json_dict.get('ticker').get('last')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('ticker').get('last') 

def getBTCfuture_index(i=0):
    if i == 0: 
        table = 'btc_future_index'
        url = 'https://www.okcoin.com/api/v1/future_index.do?symbol=btc_usd' ;
    else: 
        table = 'ltc_future_index'
        url = 'https://www.okcoin.com/api/v1/future_index.do?symbol=ltc_usd'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    row = [float(json_dict.get('future_index')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('future_index')

def getBTCthis_future_ticker(i=0):
    if i == 0: 
        table = 'btc_this_future_ticker'
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week' ;
    else: 
        table = 'ltc_this_future_ticker'
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=this_week'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    row = [float(json_dict.get('ticker').get('last')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('ticker').get('last') 

def getBTCnext_future_ticker(i=0):
    if i == 0: 
        table = 'btc_next_future_ticker'
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=next_week' ;
    else: 
        table = 'ltc_next_future_ticker'
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=next_week'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    row = [float(json_dict.get('ticker').get('last')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('ticker').get('last') 

def getBTCquarter_future_ticker(i=0):
    if i == 0: 
        table = 'btc_quarter_future_ticker'
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=quarter';
    else: 
        table = 'ltc_quarter_future_ticker'
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=quarter'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    row = [float(json_dict.get('ticker').get('last')),int(time.time())]
    insert_data(table,row)
    return json_dict.get('ticker').get('last') 
    
def get_data(i=0):   
    if i == 0: 
        data = getBTCCNY()
        # print 'BTCCNY:',data 
    elif i==1: 
        data = getExchange_rate()
        # print 'Exchange_rate:',data 
    elif i==2:
        data  = getBTCUSD()
        # print 'BTCUSD:',data
    elif i==3:
        data  = getBTCfuture_index()
        # print 'BTCfuture_index:',data
    elif i==4:
        data  = getBTCthis_future_ticker()
        # print 'BTCthis_future_ticker:',data
    elif i==5:
        data = getBTCnext_future_ticker()
        # print 'BTCnext_future_ticker:',data
    elif i==6:
        data = getBTCquarter_future_ticker()
        # print 'BTCquarter_future_ticker:',data
    elif i==7: 
        data = getBTCCNY(1)
        # print 'LTCCNY:',data   
    elif i==8: 
        data = getExchange_rate(1)
        # print 'ltc Exchange_rate:',data 
    elif i==9:
        data  = getBTCUSD(1)
        # print 'LTCUSD:',data 
    elif i==10:
        data  = getBTCfuture_index(1)
        # print 'LTCFuture_index:',data
    elif i==11:
        data  = getBTCthis_future_ticker(1)
        # print 'LTCthis_future_ticker:',data
    elif i==12:
        data = getBTCnext_future_ticker(1)
        # print 'LTCnext_future_ticker:',data
    elif i==13:
        data = getBTCquarter_future_ticker(1)
        # print 'LTCquarter_future_ticker:',data
 
def insert_data(table,data):  
    global cur
    global con  
    print table,':',data
    cur.execute('insert into '+table+' values(NULL,%s,%s)',data) 
    con.commit() 
   

if __name__ == '__main__':
 
    con = mdb.connect('localhost', 'root','', 'bit'); 
    cur = con.cursor()  

    total_field   = 14         
    thread_pool   = ThreadPool(total_field) 
    thread_list   = []
    for i in range(total_field):  
        thread_list.append(i)  

    while True: 
        # getBTCCNY()
        # getBTCCNY(1)
        # getExchange_rate()
        # getExchange_rate(1)
        # getBTCUSD()
        # getBTCUSD(1)
        # getBTCfuture_index()
        # getBTCfuture_index(1)
        # getBTCthis_future_ticker()
        # getBTCthis_future_ticker(1)
        # getBTCnext_future_ticker()
        # getBTCnext_future_ticker(1)
        # getBTCquarter_future_ticker()
        # getBTCquarter_future_ticker(1)
        thread_pool.map_async(get_data, (thread_list))
        time.sleep(1)
    # for thread in threads:
    #     thread.join()   

    # cur.execute('SELECT * FROM data ORDER BY id DESC LIMIT 1')  
    # results = cur.fetchall()
    # print results

    thread_pool.close()
    thread_pool.join()


    con.close()
 
