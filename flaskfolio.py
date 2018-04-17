from app import app, db
from app.models import User, Resume, Reference, Experience, Award, Awards, References, Experiences

print(" Welcome To FlaskFolio ")

@app.shell_context_processor
def make_shell_context():
	return {\
	'db':db,\
	'User': User,\
	'Resume': Resume,\
	'Reference': Reference,\
	'Experience': Experience,\
	'Award': Award,\
	'References': References,\
	'Experiences': Experiences,\
	'Awards': Awards,\
	}
