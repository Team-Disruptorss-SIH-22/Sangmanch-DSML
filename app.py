from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from info import finance

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('index.html')

#if route is expense then return expense per user else return reach per user
@app.route('/api/<route>')
def api(route):
	if route == 'expense':
		return finance.ExpPerUser()
	elif route == 'reach':
		return finance.ReachPerUser()
	else:
		return 'error'
@app.route('/finance/usr/<route>')
def expense(route):
	fin = finance.Finance()
	if route == 'expense':
		return fin.ExpPerUser()
	elif route == 'reach':
		return fin.ReachPerUser()
	else:
		return 'error'



if __name__ == '__main__':
	app.run(debug=True)