from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app import app
from app.models import User, Post
from app.forms import LoginForm
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/home')
def home():
	posts = [
	{'author': 'Admin', 'body': "hello, world!"},
	{'author': 'Admin', 'body': "hello, again!"}
	]
	return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.user.data).first()
		if user is None or not user.check_password(form.password.data):
			flash("invalid username or password")
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != "":
			return url_for("index")
		return redirect(next_page)
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/regester')
def regester():
	pass

@app.route('/portfolios')
def portfolios():
	return render_template('portfolio.html', title='Portfolios')

@app.route('/resumes')
def resumes():
	return render_template('resumes.html', title='Resumes')

@app.route('/donate')
def donate():
	return render_template('donate.html', title='Donate')
