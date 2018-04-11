from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from app.models import User

class LoginForm(FlaskForm):
	user = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Login')

class Regestation_form(FlaskForm):
	user = StringField("What is your Username:", validators=[DataRequired()])
	email = StringField("Email:", validators=[DataRequired(), Email()])
	password1 = PasswordField("Password:", validators=[DataRequired()])
	password2 = PasswordField("please repeat Password:", validators=[DataRequired(), EqualTo('password1')])
	submit = SubmitField("Regester!")

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError("Username alreay taken")

	def validate_email(self, email):
		check = User.query.filter_by(email=email.data)
		if check is not None:
			raise ValidationError("Email invalid or not taken")
