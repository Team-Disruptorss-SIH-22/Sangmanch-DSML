from urllib import response
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from info import finance, user
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def main():
	return render_template('index.html')


@app.route('/user/<route>')
def expense(route):
	usr = user.User()
	if route == 'expense':
		response = jsonify(usr.ExpPerUser())
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response
	elif route == 'reach':
		response =  jsonify(usr.ReachPerUser())
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response
	else:
		return 'error'

@app.route('/user/count')
def countEvent():
	usr = user.User()
	response = jsonify(usr.CountVsType())
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/user/status')
def status():
	usr = user.User()
	response = usr.reportStatus()
	response = jsonify(response)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/user/monthly')
def monthly():
	usr = user.User()
	response = jsonify(usr.monthlyData())
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response



@app.route('/ai/predict')
def ai_predict():
	pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)