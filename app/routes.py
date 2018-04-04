from flask import render_template
from app import app

@app.route("/")
@app.route("/home")
def home():
	user = {'username': 'Admin'}
	return render_template('index.html', title='Home', user=user)
