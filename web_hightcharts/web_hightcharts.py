#!/usr/bin/env python3
import flask
import random
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hightcharts_sample1/')
def hightcharts_sample1():
    return flask.render_template("hightcharts_sample1.html")


@app.route("/data1/")
def data1():
    data = {
        "title": '各城市一年资金收入情况',
        "text": '数据来源：myself.com',
        "type": 'spline',
        "yAxis_text": '金额数',
        "xAxis_text": '月份',
        "series": [{
            'name': '城市A',
            'data': [random.randint(10000, 999999) for i in range(13)]
        }, {
            'name': '城市B',
            'data': [random.randint(10000, 999999) for i in range(13)]
        }, {
            'name': '城市C',
            'data': [random.randint(10000, 999999) for i in range(13)]
        }, {
            'name': '城市D',
            'data': [random.randint(10000, 999999) for i in range(13)]
        }, {
            'name': '城市E',
            'data': [random.randint(10000, 999999) for i in range(13)]
        }]
    }
    return flask.jsonify(data)


@app.route('/hightcharts_sample2/')
def hightcharts_sample2():
    return flask.render_template("hightcharts_sample2.html")


@app.route("/data2/")
def data2():
    pass


@app.errorhandler(404)
def my_errorhandler(error):
    return "<h1>对不起，页面访问错误!</h1>", 404


@app.context_processor
def set_title():
    con = {
        "title": "hightcharts-sample"
    }
    return con


if __name__ == '__main__':
    app.run()
