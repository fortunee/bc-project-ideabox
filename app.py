from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask.ext.sqlalchemy import SQLAlchemy 
from functools import wraps



# create the application object
app = Flask(__name__)

#session key
app.secret_key = "my God is alive"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db" 


# create the sqlachemy object
db = SQLAlchemy(app)

from models import *

# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

# handles the welcome page
@app.route("/welcome")
def welcome():
	return render_template('welcome.html', title="Welcome to Ideabox")


# handles the signup page
@app.route("/signup", methods=['GET', 'POST'])
def signup():
	return render_template('signup.html', title="Signup")



# handles the login page
@app.route("/login", methods=['GET', 'POST'])
def login():

	print 'route hit'
	error_msg = None
	if request.method == 'POST':	
		if request.form['username'] != 'fortune' \
			or request.form['password'] != 'test':
			error = 'Invalid login'
		else:
			session['logged_in'] = True
			flash("login successful")
			return redirect(url_for('home'))

	return render_template('login.html', error_msg=error_msg, title="Please login")

# handles the home page
@app.route('/')
@login_required
def home():
	posts = db.session.query(IdeaPost).all()
	return render_template('index.html', posts=posts, title="Ideabox | Home")


# handles the post making page
@app.route('/post')
@login_required
def post():
	return render_template('post.html', title="Share an Idea")


# handles the profile 
@app.route('/profile')
@login_required
def profile():
	return render_template('profile.html', title="Profile")



# handles user logouts
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You are logged out')
	return redirect(url_for('welcome'))


# this maps the contact us page
@app.route('/contact')
def contact():
	return render_template('contact.html', title='Contact')


# maps the about us page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

"""def connect_db():
	return sqlite3.connect('posts.db')"""

if __name__ == "__main__":
	app.run(debug=True)