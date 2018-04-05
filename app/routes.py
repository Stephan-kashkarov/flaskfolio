from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
	user = {'username': 'Admin'}
	return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
	return

@app.route('/portfolios')
def portfolios():
	return render_template('portfolio.html', title='portfolios')

@app.route('/resumes')
def resumes():
	return render_template('resumes.html', title='resumes')

@app.route('/donate')
def donate():
	return render_template('donate.html', title='donate')
