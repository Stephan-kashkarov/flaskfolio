from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
	user = {'username': 'Admin'}
	return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

@app.route('/portfolios')
def portfolios():
	return render_template('portfolio.html', title='Portfolios')

@app.route('/resumes')
def resumes():
	return render_template('resumes.html', title='Resumes')

@app.route('/donate')
def donate():
	return render_template('donate.html', title='Donate')
