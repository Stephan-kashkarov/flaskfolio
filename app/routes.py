from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
	user = {'username': 'Admin'}
	return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for {}, Remember Me = {}' .format(
			form.user.data,
			form.remember_me.data
		))
		return redirect('url_for(home)')
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
