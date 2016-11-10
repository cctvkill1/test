# -*- coding: utf-8 -*- 
import datetime
import json  
import time
import MySQLdb as mdb


def getSqlData(sql):  
	con     = mdb.connect('localhost', 'root','123456', 'bit'); 
	cur     = con.cursor()     
	count   = cur.execute(sql)  
	results = cur.fetchall()	
	con.close()
	return results

def serialize(results):
	data    = []
	for r in results: 
		row = []
		row.append(datetime.datetime.fromtimestamp(int(r[1])).strftime('%Y-%m-%d %H:%M:%S'))
		row.append(float(r[0]))   
		data.append(row) 
	data = json.dumps(data)    
	return data

def TotalSerialize(results):
	data    = []
	for r in results: 
		row = []
		row.append(r[0])
		row.append(float(r[1]))   
		data.append(row) 
	data = json.dumps(data)    
	return data


def data(limit = '1000'): 
	limit                     = str(limit)
	btc                       = serialize(getSqlData('select `value`,ct from btc_cny order by id desc limit 0,'+limit))
	btc_exchange_rate         = serialize(getSqlData('select `value`,ct from btc_exchange_rate order by id desc limit 0,'+limit))   
	btc_future_index          = serialize(getSqlData('select `value`,ct from btc_future_index order by id desc limit 0,'+limit))
	btc_next_future_ticker    = serialize(getSqlData('select `value`,ct from btc_next_future_ticker order by id desc limit 0,'+limit))
	btc_quarter_future_ticker = serialize(getSqlData('select `value`,ct from btc_quarter_future_ticker order by id desc limit 0,'+limit))
	btc_this_future_ticker    = serialize(getSqlData('select `value`,ct from btc_this_future_ticker order by id desc limit 0,'+limit))
	btc_usd                   = serialize(getSqlData('select `value`,ct from btc_usd order by id desc limit 0,'+limit)) 

 	result =  [btc,btc_exchange_rate,btc_future_index,btc_next_future_ticker,btc_quarter_future_ticker,btc_this_future_ticker,btc_usd]

 	return  result
 
def dataltc(limit = '1000'): 
	limit                     = str(limit)
	ltc                       = serialize(getSqlData('select `value`,ct from ltc_cny order by id desc limit 0,'+limit))
	ltc_exchange_rate         = serialize(getSqlData('select `value`,ct from ltc_exchange_rate order by id desc limit 0,'+limit)) 
	ltc_future_index          = serialize(getSqlData('select `value`,ct from ltc_future_index order by id desc limit 0,'+limit))
	ltc_next_future_ticker    = serialize(getSqlData('select `value`,ct from ltc_next_future_ticker order by id desc limit 0,'+limit))
	ltc_quarter_future_ticker = serialize(getSqlData('select `value`,ct from ltc_quarter_future_ticker order by id desc limit 0,'+limit))
	ltc_this_future_ticker    = serialize(getSqlData('select `value`,ct from ltc_this_future_ticker order by id desc limit 0,'+limit))
	ltc_usd                   = serialize(getSqlData('select `value`,ct from ltc_usd order by id desc limit 0,'+limit)) 

 	result =  [ltc,ltc_exchange_rate,ltc_future_index,ltc_next_future_ticker,ltc_quarter_future_ticker,ltc_this_future_ticker,ltc_usd]

 	return  result
 

def getTotal():
	timeEnd            		  = str(int(time.time()))
	timeStart                 = str(int(time.time())-86400*7)
	btc                       = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_cny  where ct < "+timeEnd+" && ct > "+ timeStart+" GROUP BY tct"))
	btc_exchange_rate         = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_exchange_rate  where ct < "+timeEnd+" && ct > "+ timeStart+" GROUP BY tct")) 
	btc_future_index          = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_future_index  where ct < "+timeEnd+" && ct > "+ timeStart+" GROUP BY tct"))
	btc_next_future_ticker    = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_next_future_ticker  where ct < "+timeEnd+" && ct > "+ timeStart+" GROUP BY tct"))
	btc_quarter_future_ticker = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_quarter_future_ticker  where ct < "+timeEnd+" && ct > "+ timeStart+" GROUP BY tct"))
	btc_this_future_ticker    = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_this_future_ticker  where ct < "+timeEnd+" && ct > "+ timeStart+" GROUP BY tct"))
	btc_usd                   = TotalSerialize(getSqlData("SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_usd  where ct < "+timeEnd+" && ct > "+ timeStart+"  GROUP BY tct")) 
 
 	result =  [btc,btc_exchange_rate,btc_future_index,btc_next_future_ticker,btc_quarter_future_ticker,btc_this_future_ticker,btc_usd]
 	return result;