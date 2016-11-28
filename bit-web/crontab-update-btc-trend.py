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

def commitSqlData(sql):  
	con     = mdb.connect('localhost', 'root','123456', 'bit'); 
	cur     = con.cursor()     
	cur.execute(sql)   
	con.commit()  
	con.close() 

def runSql(): 
	getLastTimeSql = 'select time from btc_trend where id = (select max(id) from btc_trend)'
	getLastTime = getSqlData(getLastTimeSql) 
	lastTime = str(int(time.mktime( getLastTime[0][0].timetuple())))  
	insert_btc_future_index_sql = " INSERT INTO btc_trend  (time,btc_future_index) SELECT  time,btc_future_index  FROM   (   SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,  	 avg(`value`) btc_future_index      FROM btc_future_index where ct>"+lastTime+"  GROUP BY  time     ) b  ";
	update_btc_this_future_ticker_sql = '''
	update btc_trend x, 
	(
	select a.time,a.btc_this_future_ticker from (
	SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,
	avg(`value`) btc_this_future_ticker 
	FROM btc_this_future_ticker where ct>'''+lastTime+'''  GROUP BY  time   
	) a   left JOIN btc_trend b on a.time = b.time) y 
	set x.btc_this_future_ticker = y.btc_this_future_ticker
	where  x.time = y.time ;'''

	update_btc_next_future_ticker_sql = ''' 
	update btc_trend x, 
	(
	select a.time,a.btc_next_future_ticker from (
	SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,
	 avg(`value`) btc_next_future_ticker 
	FROM btc_next_future_ticker where ct>'''+lastTime+'''  GROUP BY  time   
	) a   left JOIN btc_trend b on a.time = b.time) y 
	set x.btc_next_future_ticker = y.btc_next_future_ticker
	where  x.time = y.time ;'''

	update_btc_quarter_future_ticker_sql = '''  
	update btc_trend x, 
	(
	select a.time,a.btc_quarter_future_ticker from (
	SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,
	avg(`value`) btc_quarter_future_ticker 
	FROM btc_quarter_future_ticker where ct>'''+lastTime+'''  GROUP BY  time   
	) a   left JOIN btc_trend b on a.time = b.time) y 
	set x.btc_quarter_future_ticker = y.btc_quarter_future_ticker
	where  x.time = y.time ;
	'''

	update_btc_cny_sql = '''  
	update btc_trend x, 
	(
	select a.time,a.btc_cny from (
	SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,
	avg(`value`) btc_cny 
	FROM btc_cny where ct>'''+lastTime+'''  GROUP BY  time   
	) a   left JOIN btc_trend b on a.time = b.time) y 
	set x.btc_cny = y.btc_cny
	where  x.time = y.time ;
	'''

	update_btc_exchange_rate_sql = '''  
	update btc_trend x, 
	(
	select a.time,a.btc_exchange_rate from (
	SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,
	avg(`value`) btc_exchange_rate 
	FROM btc_exchange_rate where ct>'''+lastTime+'''  GROUP BY  time   
	) a   left JOIN btc_trend b on a.time = b.time) y 
	set x.btc_exchange_rate = y.btc_exchange_rate
	where  x.time = y.time ;
	'''
	update_btc_usd_sql = '''  
	update btc_trend x, 
	(
	select a.time,a.btc_usd from (
	SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') as 'time' ,
	avg(`value`) btc_usd 
	FROM btc_usd where ct>'''+lastTime+'''  GROUP BY  time   
	) a   left JOIN btc_trend b on a.time = b.time) y 
	set x.btc_usd = y.btc_usd
	where  x.time = y.time ;
	'''

	commitSqlData(insert_btc_future_index_sql) 
	commitSqlData(update_btc_this_future_ticker_sql)
	commitSqlData(update_btc_next_future_ticker_sql)
	commitSqlData(update_btc_quarter_future_ticker_sql)
	commitSqlData(update_btc_cny_sql)
	commitSqlData(update_btc_exchange_rate_sql)
	commitSqlData(update_btc_usd_sql)
 	
 	print 'ok';
if __name__ == '__main__':
	runSql()