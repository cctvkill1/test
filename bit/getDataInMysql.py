# -*- coding: utf-8 -*- 
import time
import MySQLdb as mdb
   
 
def insert_data(table,rowData):   
	if rowData==None: 
		return False
    con = mdb.connect('localhost', 'root','123456', 'bit'); 
    cur = con.cursor()    
    row = []
    row.append(float(rowData))  
    row.append(int(time.time()))
    print table,':',row
    cur.execute('insert into '+table+' values(NULL,%s,%s)',row) 
    con.commit()  
    con.close()
   
 