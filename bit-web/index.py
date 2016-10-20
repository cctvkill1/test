# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,request
import datetime 
import json  
from getData import data

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

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)