# -*- coding: utf-8 -*- 
import datetime
import json  
import time
import pymysql as mdb


def getSqlData(sql):  
	con     = mdb.connect('localhost', 'root','', 'lianjia',charset='utf8'); 
	cur     = con.cursor()     
	count   = cur.execute(sql)  
	results = cur.fetchall()	
	con.close()
	return results


def data(): 
	results                       = getSqlData('select lng,lat,name from house')  
	return  results 

def data_info(): 
	results                       = getSqlData('select lng,lat,name,price,total,date,info from house')    
	data    = []
	for r in results: 
		row = [] 
		row.append(str(r[0])) 
		row.append(str(r[1])) 
		row.append(str(r[2])) 
		row.append(str(r[3])) 
		row.append(str(r[4])) 
		row.append(str(r[5])) 
		row.append(str(r[6]))   
		data.append(row)   
	return  data