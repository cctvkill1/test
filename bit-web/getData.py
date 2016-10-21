# -*- coding: utf-8 -*- 
import datetime
import json  
import MySQLdb as mdb 

def getSqlData(sql):  
	con     = mdb.connect('localhost', 'root','', 'bit'); 
	cur     = con.cursor()     
	count   = cur.execute(sql)  
	results = cur.fetchall()	
	data    = []
	for r in results: 
		row = []
		row.append(datetime.datetime.fromtimestamp(int(r[1])).strftime('%Y-%m-%d %H:%M:%S'))
		row.append(float(r[0]))   
		data.append(row) 
	data = json.dumps(data)   
	con.close()
	return data

def data(limit = '1000'): 
	limit                     = str(limit)
	btc                       = getSqlData('select `value`,ct from btc_cny order by id desc limit 0,'+limit)
	btc_exchange_rate         = getSqlData('select `value`,ct from btc_exchange_rate order by id desc limit 0,'+limit)   
	btc_future_index          = getSqlData('select `value`,ct from btc_future_index order by id desc limit 0,'+limit)
	btc_next_future_ticker    = getSqlData('select `value`,ct from btc_next_future_ticker order by id desc limit 0,'+limit)
	btc_quarter_future_ticker = getSqlData('select `value`,ct from btc_quarter_future_ticker order by id desc limit 0,'+limit)
	btc_this_future_ticker    = getSqlData('select `value`,ct from btc_this_future_ticker order by id desc limit 0,'+limit)
	btc_usd                   = getSqlData('select `value`,ct from btc_usd order by id desc limit 0,'+limit) 

 	result =  [btc,btc_exchange_rate,btc_future_index,btc_next_future_ticker,btc_quarter_future_ticker,btc_this_future_ticker,btc_usd]

 	return  result
 
def dataltc(limit = '1000'): 
	limit                     = str(limit)
	ltc                       = getSqlData('select `value`,ct from ltc_cny order by id desc limit 0,'+limit)
	ltc_exchange_rate         = getSqlData('select `value`,ct from ltc_exchange_rate order by id desc limit 0,'+limit)   
	ltc_future_index          = getSqlData('select `value`,ct from ltc_future_index order by id desc limit 0,'+limit)
	ltc_next_future_ticker    = getSqlData('select `value`,ct from ltc_next_future_ticker order by id desc limit 0,'+limit)
	ltc_quarter_future_ticker = getSqlData('select `value`,ct from ltc_quarter_future_ticker order by id desc limit 0,'+limit)
	ltc_this_future_ticker    = getSqlData('select `value`,ct from ltc_this_future_ticker order by id desc limit 0,'+limit)
	ltc_usd                   = getSqlData('select `value`,ct from ltc_usd order by id desc limit 0,'+limit) 

 	result =  [ltc,ltc_exchange_rate,ltc_future_index,ltc_next_future_ticker,ltc_quarter_future_ticker,ltc_this_future_ticker,ltc_usd]

 	return  result
 