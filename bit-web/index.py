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




# BTC图表：（先选择时间区间查看）
# 美金指数修正：BTCfuture_index - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# 现货VS本周：竖轴值：BTCthis_future_ticker - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# 现货VS次周：竖轴值：BTCnext_future_ticker - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# 现货VS季度：竖轴值：BTCquarter_future_ticker - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# LTC图表：（先选择时间区间查看）
# 美金指数修正：LTCfuture_index - （LTCCNY /Exchange_rate+LTCUSD）/2,横轴值：时间
# 现货VS本周：竖轴值：LTCthis_future_ticker - （LTCCNY /Exchange_rate+LTCUSD）/2,横轴值：时间
# 现货VS次周：竖轴值：LTCnext_future_ticker - （LTCCNY /Exchange_rate+LTCUSD）/2,横轴值：时间
# 现货VS季度：竖轴值：LTCquarter_future_ticker - （LTCCNY /Exchange_rate+LTCUSD）/2,横轴值：时间

@app.route('/btcTable')
def btcTable(name=None): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')	   
	result = data() 
	return render_template('btcTable.html', name=name,echart=echart,jquery=jquery,result=result)

@app.route('/getDataBtcTable',methods=['GET', 'POST'])
def getDataBtcTable(): 	 
	if request.method == 'POST':
		result = data(1) 
		result = json.dumps(result)   
		return result
	else:
		return '405' 




if __name__ == '__main__':
	# app.run()
	app.debug=True
	app.run('192.168.31.149')