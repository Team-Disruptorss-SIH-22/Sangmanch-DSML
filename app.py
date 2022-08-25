from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from info import finance, user
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def main():
	return render_template('index.html')


@app.route('/user/<route>')
def expense(route):
	usr = user.User()
	if route == 'expense':
		return usr.ExpPerUser()
	elif route == 'reach':
		return usr.ReachPerUser()
	else:
		return 'error'

@app.route('/user/count')
def countEvent():
	usr = user.User()
	return usr.CountVsType()

@app.route('/user/status')
def status():
	usr = user.User()
	return usr.reportStatus()

@app.route('/user/monthly')
def monthly():
	usr = user.User()
	return usr.monthlyData()



@app.route('/ai/predict')
def ai_predict():
	pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)