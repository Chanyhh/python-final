# -*- coding:utf-8 -*-
from flask import Flask,request,redirect,jsonify,render_template,Response,make_response
import json
import os
from shutil import copytree,rmtree
import pandas as pd

app = Flask(__name__)

list = ['病床使用情况', '各卫生机构床位数', '每年病床工作日', '每年各机构床位数对比', '使用率与平均住日']


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/front',methods=['GET'])
def front():
    return render_template('front.html')

@app.route('/speech',methods=['GET'])
def speech():
    return render_template('speech.html')

@app.route('/analysis_one',methods=['GET'])
def analysis_one():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/liyonglv.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data_html = result.to_html( )
    return render_template('analysis_one.html',the_res = data_html,list=list)

@app.route('/analysis_two',methods=['GET'])
def analysis_two():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/chuangweishu.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data_html = result.to_html( )
    return render_template('analysis_two.html',the_res = data_html,list=list)

@app.route('/analysis_three',methods=['GET'])
def analysis_three():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/liyonglv.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data_html = result.to_html( )
    return render_template('analysis_three.html',the_res = data_html,list=list)

@app.route('/analysis_four',methods=['GET'])
def analysis_four():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/chuangweishu.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data_html = result.to_html( )
    return render_template('analysis_four.html',the_res = data_html,list=list)

@app.route('/analysis_five',methods=['GET'])
def analysis_five():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/chuangweishu.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data_html = result.to_html( )
    return render_template('analysis_five.html',the_res = data_html,list=list)

@app.route('/skip',methods=['POST'])
def skip():

    stand = {
        "病床使用情况":"analysis_one",
        "各卫生机构床位数":"analysis_two",
        "每年病床工作日":"analysis_three",
        "每年各机构床位数对比":"analysis_four",
        "使用率与平均住日":"analysis_five"
    }

    option = request.form['option']
    print(option)
    return redirect('/{}'.format(stand[option]))


if __name__ == '__main__':
    app.run(debug=True,port=8080)