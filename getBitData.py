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
    global total_field
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

    row[i] = float(data)
    count += 1 
    # print '----',i,row[i],'==',count,'--',total_field
    if count==total_field:
        print '=========================over========================='
        # print '---row:',row
        insert_data()
  
def insert_data(): 
    global row
    global cur
    global con
    global total_field

 
    row[total_field] = float(time.time());  
    flag = False
    index_list = []  
    for x in range(total_field):
        if row[x]==0: 
            flag = True
            index_list.append(x)  
    if flag:        
        cur.execute('SELECT * FROM data ORDER BY id DESC LIMIT 1')  
        results = cur.fetchall()
        for index in index_list:
            print '处理',index
            row[index] = results[index+1]

    print '=row:',row
    cur.execute('insert into data values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row) 
    con.commit() 
   

if __name__ == '__main__':

    # con = None
    # try: 
    #     con = mdb.connect('localhost', 'root','', 'bit'); 
    #     cur = con.cursor()  

    #     total_field   = 14
    #     count         = 0
    #     row           = []
    #     thread_pool   = ThreadPool(total_field) 
    #     thread_list   = []
    #     for i in range(total_field):  
    #         thread_list.append(i) 
    #     while True:
    #         count = 0
    #         row   = [0]*(total_field+1)
    #         thread_pool.map_async(get_data, (thread_list))
    #         time.sleep(1)

    #     cur.execute('SELECT * FROM data ORDER BY id DESC LIMIT 1')  
    #     results = cur.fetchall()
    #     print results

    #     thread_pool.close()
    #     thread_pool.join()

    # finally:
    #   if con: 
    #     con.close()
 