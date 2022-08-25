from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from info import finance, user
import sys

app = Flask(__name__)


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


if __name__ == '__main__':
	app.run(debug=True)