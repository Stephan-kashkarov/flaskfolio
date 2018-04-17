from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from app import db
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	user_id = db.Column(db.Integer, primary_key=True, nullable=False)
	username = db.Column(db.String(30), index=True, unique=True, nullable=False)
	email = db.Column(db.String(120), index=True, unique=True)
	pass_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.pass_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pass_hash, password)

class Resume(db.Model):
	resume_id = db.Column(db.Integer, primary_key=True, nullable=False)
	user_id = db.relationship(db.Integer, db.ForeignKey('User.user_id'))
	pinned = db.Column(db.Boolean)
	references = db.relationship('references', backref='resume', lazy=True)
	awards = db.relationship('awards', backref='resume', lazy=True)
	experiences = db.relationship('experiences', backref='resume', lazy=True)

	def __repr__(self):
		return "<User_id {}'s resume, id {}>".format(user_id, resume_id)

class Reference(db.Model):
	reference_id = db.Column(db.Integer, primary_key=True, nullable=False)
	reference_name = db.Column(db.String(100))
	title = db.Column(db.String(50))
	company = db.Column(db.String(100))
	phone = db.Column(db.Integer)
	email = db.Column(db.String(100))

	def __repr__(self):
		return "<Reference: {} at {} who is a {}. Contact: phone, {} email, {}>"\
		.format(reference_name, company, title, phone, email)

class Experience(db.Model):
	experience_id = db.Column(db.Integer, primary_key=True, nullable=False)
	location = db.Column(db.String(100))
	title = db.Column(db.String(100))
	start_date = db.Column(db.DateTime)
	end_date = db.Column(db.DateTime)

	def __repr__(self):
		return "<Experice: {} at {} from {} to {}>"\
		.format(title, location, start_date, end_date)

class Award(db.Model):
	award_id = db.Column(db.Integer, primary_key=True, nullable=False)
	award_name = db.Column(db.String(100))
	award_date = db.Column(db.DateTime)

class Awards(db.Model):
	resume_id = db.Column(db.Integer, db.ForeignKey('resume.resume_id'), primary_key=True)
	award_id = db.Column(db.Integer, db.ForeignKey('award.award_id'), primary_key=True)

class References(db.Model):
	resume_id = db.Column(db.Integer, db.ForeignKey('resume.resume_id'), primary_key=True)
	reference_id = db.Column(db.Integer, db.ForeignKey('reference.reference_id'), primary_key=True)

class Experiences(db.Model):
	resume_id = db.Column(db.Integer, db.ForeignKey('resume.resume_id'), primary_key=True)
	experience_id = db.Column(db.Integer, db.ForeignKey('experience.experience_id'), primary_key=True)
