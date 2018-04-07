import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'work-is-for-the-weak!'

	SQLALCHEMY_DATABASE_URI = os.environ.geT('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
