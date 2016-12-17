# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,request,jsonify
import datetime 
import json    
import getData as gd

app = Flask(__name__)  

@app.route('/')
def index():  
	echart = url_for('static', filename='echarts.min.js') 
	jquery = url_for('static', filename='jquery.min.js')	 
	return render_template('index.html',echart=echart,jquery=jquery)
 
   
@app.route('/getData',methods=['GET', 'POST'])
def getData(): 	 
	if request.method == 'POST':
		result = gd.data() 
		result = json.dumps(result)   
		return result
	else:
		return '405' 

@app.route('/map')
def map():  
	echart = url_for('static', filename='echarts.min.js') 
	jquery = url_for('static', filename='jquery.min.js')	 
	return render_template('map.html',echart=echart,jquery=jquery,json=json)
 
@app.route('/getDataInfo',methods=['GET', 'POST'])
def getDataInfo(): 	 
	if request.method == 'POST':
		result = gd.data_info() 
		result = json.dumps(result)   
		return result
	else:
		return '405' 



if __name__ == '__main__':
	app.debug=True 
	app.run()
	# app.run(host="172.17.9.119",port=80,threaded=True)  