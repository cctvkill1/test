# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,request,jsonify
import datetime 
import json  
import getData as gd
from flask.ext.cache import Cache

app = Flask(__name__) 
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

@app.route('/')
def index():  
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')	   
	result = gd.data()  
	result = json.dumps(result)  
	return render_template('index.html',echart=echart,jquery=jquery,result=result)

@app.route('/getData',methods=['GET', 'POST'])
def getData(): 	 
	if request.method == 'POST':
		result = gd.data(1) 
		result = json.dumps(result)   
		return result
	else:
		return '405' 

@app.route('/trend')
def trend(): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')
	return render_template('trend.html', echart=echart,jquery=jquery)
 
@app.route('/getTrendData')
def getTrendData(): 	 
	skip = request.args.get('page') 
	if not skip: 
		skip = '1'
	limit = request.args.get('limit');
	if not limit: 	   
		limit = '1000'
	skip = str((int(skip)-1)*int(limit))
	result = gd.dataTrend(skip,limit) 
	result = json.dumps(result)  
	return result
 
# btc 实时变化图标
@app.route('/btcTable')
def btcTable(): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js')	   
	result = gd.data() 
	return render_template('btcTable.html', echart=echart,jquery=jquery,result=result)
@app.route('/getDataBtcTable',methods=['GET', 'POST'])
def getDataBtcTable(): 	 
	if request.method == 'POST':
		result = gd.data(1) 
		result = json.dumps(result)   
		return result
	else:
		return '405' 


# // # BTC图表：（先选择时间区间查看）
# // # 美金指数修正：BTCfuture_index - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# // # 现货VS本周：竖轴值：BTCthis_future_ticker - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# // # 现货VS次周：竖轴值：BTCnext_future_ticker - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# // # 现货VS季度：竖轴值：BTCquarter_future_ticker - （BTCCNY /Exchange_rate+BTCUSD）/2,横轴值：时间
# //   0    1                        2              3                      4                      5                       6
# // [btc,btc_exchange_rate,btc_future_index,btc_next_future_ticker,btc_quarter_future_ticker,btc_this_future_ticker,btc_usd]

		
# btc 一周统计图
@app.route('/btctt')
@cache.cached(timeout=600) 
def btctt(): 
	echart = url_for('static', filename='echarts.min.js')
	jquery = url_for('static', filename='jquery.min.js') 
	return render_template('btctt.html',echart=echart,jquery=jquery)
 

# btc 一周统计图数据
@app.route('/btcttData')
@cache.cached(timeout=600) 
def btcttData():  	   
	result = gd.getTotal() 
	result = json.dumps(result)   
	return result
  


if __name__ == '__main__':
	app.debug=True 
	app.run()
	# app.run(host="172.17.9.119",port=80,threaded=True)  