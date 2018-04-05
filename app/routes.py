from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
	user = {'username': 'Admin'}
	return render_template('index.html', title='Home', user=user)

@app.route('/portfolios')
def portfolios():
	return render_template('portfolios.html')

@app.route('/resumes')
def resumes():
	return 'Resumes'

@app.route('/donate')
def donate():
	return 'support me!'
