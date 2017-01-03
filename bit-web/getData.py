# -*- coding: utf-8 -*- 
import datetime
import json  
import time
import pymysql as mdb


def getSqlData(sql):  
	con     = mdb.connect('localhost', 'root','', 'bit'); 
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
	results                       = getSqlData('SELECT btc_future_index.ct, btc_future_index.`value`, btc_this_future_ticker.`value`, btc_next_future_ticker.`value`, btc_quarter_future_ticker.`value` FROM btc_future_index INNER JOIN btc_this_future_ticker ON btc_future_index.ct = btc_this_future_ticker.ct INNER JOIN btc_next_future_ticker ON btc_future_index.ct = btc_next_future_ticker.ct INNER JOIN btc_quarter_future_ticker ON btc_future_index.ct = btc_quarter_future_ticker.ct ORDER BY	btc_future_index.id DESC LIMIT 0,'+limit) 
	data    = []
	for r in results: 
		row = []
		row.append(datetime.datetime.fromtimestamp(int(r[0])).strftime('%Y-%m-%d %H:%M:%S'))
		row.append(float(r[1])) 
		row.append(float(r[2])) 
		row.append(float(r[3])) 
		row.append(float(r[4]))   
		data.append(row) 
	# data = json.dumps(results)    
	return  data
 
def dataTrend(skip='0',limit = '1000'):   
	skip                      = str(skip)
	limit                     = str(limit)
	results                       = getSqlData('select time,btc_future_index,btc_this_future_ticker,btc_next_future_ticker,btc_quarter_future_ticker,btc_cny,btc_exchange_rate,btc_usd from btc_trend order by id desc limit '+skip+', '+limit)  
	data    = []
	for r in results: 
		row = []
		row.append(r[0].strftime('%Y-%m-%d %H:%M'))
		if r[1]:
			row.append(float(r[1])) 
		else:
			row.append(0)
		if r[2]:
			row.append(float(r[2])) 
		else:
			row.append(0)
		if r[3]:
			row.append(float(r[3])) 
		else:
			row.append(0)
		if r[4]:
			row.append(float(r[4])) 
		else:
			row.append(0)   
		if r[5]:
			row.append(float(r[5])) 
		else:
			row.append(0)
		if r[6]:
			row.append(float(r[6])) 
		else:
			row.append(0)
		if r[7]:
			row.append(float(r[7])) 
		else:
			row.append(0)
		data.append(row)   
	return  data
 

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