import sqlite3

with sqlite3.connect("members.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE  if not exists idea(firstname varchar, lastname varchar, email varchar, password)""")
	c.execute('INSERT INTO idea(firstname, lastname, email, password) VALUES("fortune", "ekeruo", "legalmody@gmail.com", "admin")')

	c.execute("""CREATE TABLE if not exists posts(title TEXT, description TEXT)""")
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("well", "I love your idea")')

	
	