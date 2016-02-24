from flask import Flask, render_template, request, redirect, url_for, session, flash, g
import sqlite3
from functools import wraps

# create the application object
app = Flask(__name__)

#session key
app.secret_key = "my God is alive"

app.database = "members.db"

# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if "logged_in" in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('welcome'))
	return wrap

# handles the welcome page
@app.route("/welcome")
def welcome():
	return render_template('welcome.html', title="Welcome to Ideabox")

# handles the signup page
@app.route("/signup")
def signup():
	return render_template('signup.html', title="Signup")

# handles the login page
@app.route("/login", methods=['GET', 'POST'])
def login():
	error_msg = None
	g.db = connect_db()
	if request.method == 'POST':
		cur = g.db.execute("SELECT * FROM idea WHERE email = (%s)",
							thwart(request.form['username']))
		cur = g.db.fetchall()[3]
		if request.form['username'] != username \
		or request.form['password'] != password:
			error_msg = 'Invalid login credentials, try again'
		else:
			session['logged_in'] = True
			flash('successfully logged in')
			return redirect(url_for('home'))
	return render_template('login.html', error_msg=error_msg, title="Please login")

# handles the home page
@app.route('/')
@login_required
def home():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	g.db.close()
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
	return redirect(url_for('welcome'))

# this maps the contact us page
@app.route('/contact')
def contact():
	return render_template('contact.html', title='Contact')

# maps the about us page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

# initialization of db connection
def connect_db():
	return sqlite3.connect(app.database)

if __name__ == "__main__":
	app.run(debug=True)