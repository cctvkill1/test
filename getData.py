# encoding=utf-8
import urllib2
import json  
from multiprocessing.dummy import Pool as ThreadPool
from threading import Thread
import sys 
import time
import MySQLdb as mdb
  
def getBTCCNY(i=0): 
    if i == 0: 
        url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny' ;
    else: 
        url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny';
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('ticker').get('last') 

def getExchange_rate(i=0):
    if i == 0: 
        url = 'https://www.okcoin.com/api/v1/exchange_rate.do' ;
    else: 
        url = 'https://www.okcoin.com/api/v1/exchange_rate.do';
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('rate')

def getBTCUSD(i=0):
    if i == 0: 
        url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd' ;
    else: 
        url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('ticker').get('last') 

def getBTCfuture_index(i=0):
    if i == 0: 
        url = 'https://www.okcoin.com/api/v1/future_index.do?symbol=btc_usd' ;
    else: 
        url = 'https://www.okcoin.com/api/v1/future_index.do?symbol=ltc_usd'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('future_index')

def getBTCthis_future_ticker(i=0):
    if i == 0: 
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week' ;
    else: 
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=this_week'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('ticker').get('last') 

def getBTCnext_future_ticker(i=0):
    if i == 0: 
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=next_week' ;
    else: 
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=next_week'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('ticker').get('last') 

def getBTCquarter_future_ticker(i=0):
    if i == 0: 
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=quarter';
    else: 
        url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=ltc_usd&contract_type=quarter'; 
    data      = urllib2.urlopen(url).read() 
    json_dict = json.loads(data)   
    return json_dict.get('ticker').get('last') 
    
def get_data(i=0):  
    global count
    global row
    if i == 0: 
        data = getBTCCNY()
        print 'BTCCNY:',data 
    elif i==1: 
        data = getExchange_rate()
        print 'Exchange_rate:',data 
    elif i==2:
        data  = getBTCUSD()
        print 'BTCUSD:',data
    elif i==3:
        data  = getBTCfuture_index()
        print 'BTCfuture_index:',data
    elif i==4:
        data  = getBTCthis_future_ticker()
        print 'BTCthis_future_ticker:',data
    elif i==5:
        data = getBTCnext_future_ticker()
        print 'BTCnext_future_ticker:',data
    elif i==6:
        data = getBTCquarter_future_ticker()
        print 'BTCquarter_future_ticker:',data
    if i == 7: 
        data = getBTCCNY(1)
        print 'LTCCNY:',data   
    elif i==8: 
        data = getExchange_rate(1)
        print 'ltc Exchange_rate:',data 
    elif i==9:
        data  = getBTCUSD(1)
        print 'LTCUSD:',data 
    elif i==10:
        data  = getBTCfuture_index(1)
        print 'LTCFuture_index:',data
    elif i==11:
        data  = getBTCthis_future_ticker(1)
        print 'LTCthis_future_ticker:',data
    elif i==12:
        data = getBTCnext_future_ticker(1)
        print 'LTCnext_future_ticker:',data
    elif i==13:
        data = getBTCquarter_future_ticker(1)
        print 'LTCquarter_future_ticker:',data

    row.insert(i, float(data));  
    count += 1
    if count==14:
        print '=========================over========================='
        insert_data(row)
  
def insert_data(row): 
    print row
    global cur
    global con

    cur.executemany("insert into data values (%s,%s,%s,%s,%s,%s,%s)", row) 
 
    con.commit()
   

if __name__ == '__main__':

    con = None
    try: 
        con = mdb.connect('localhost', 'root','', 'bit'); 
        cur = con.cursor() 
        row = [4328.14, 6.6728, 635.17, 26.17, 643.59, 645.35, 3.917, 646.56, 670.92, 6.6728, 3.893, 4.084, 3.84, 3.898]
        # data = tuple(row)
        print row[0]
        T = ('1','1','10','1','10','1','atyu30','2','1','10','1','10','1','atyu30')
        # cur.executemany("insert into data values ("+str(T)+")") 
        cur.execute("INSERT INTO data VALUES(%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)" %  tuple(row))
        # cur.execute("INSERT INTO data SET Data='%s'" %mdb.escape_string(img))
        con.commit()
        # totalPage = 14
        # page_pool = ThreadPool(totalPage) 
        # page_list = []
        # for i in range(0, totalPage):  
        #     page_list.append(i)
        # while True:
        #     count     = 0
        #     row = []
        #     page_pool.map_async(get_data, (page_list))
        #     time.sleep(1)

        # page_pool.close()
        # page_pool.join()

    finally:
      if con: 
        con.close()
 