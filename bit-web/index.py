# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,request
import datetime 
import json  
from getData import data,dataltc

app = Flask(__name__) 

@app.route('/')
def index(name=None): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')	   
	result = data() 
	return render_template('index.html', name=name,echart=echart,jquery=jquery,result=result)

@app.route('/getData',methods=['GET', 'POST'])
def getData(): 	 
	if request.method == 'POST':
		result = data(1) 
		result = json.dumps(result)   
		return result
	else:
		return '405' 

@app.route('/ltc')
def ltc(name=None): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')	   
	result = dataltc() 
	return render_template('ltc.html', name=name,echart=echart,jquery=jquery,result=result)

@app.route('/getDataLtc',methods=['GET', 'POST'])
def getDataLtc(): 	 
	if request.method == 'POST':
		result = dataltc(1) 
		result = json.dumps(result)   
		return result
	else:
		return '405' 
 
# btc 实时变化图标
@app.route('/btctt')
def btcTable(name=None): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')	   
	result = data() 
	return render_template('btctt.html', name=name,echart=echart,jquery=jquery,result=result)
@app.route('/getDataBtcTable',methods=['GET', 'POST'])
def getDataBtcTable(): 	 
	if request.method == 'POST':
		result = data(1) 
		result = json.dumps(result)   
		return result
	else:
		return '405' 


# SELECT FROM_UNIXTIME(ct,'%Y-%m-%d %H:%i') tct , avg(`value`) 'value'  FROM btc_cny  where ct < 1477617431 GROUP BY tct

if __name__ == '__main__':
	# app.run()
	app.debug=True
	app.run('port=80')