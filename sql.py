import sqlite3

with sqlite3.connect("sample.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
	c.execute(
		"""INSERT INTO posts VALUES("Jump out of the earth", 
			"You can walk straight into the end of the world, 
			or fall in to the pacific and swim to enternity 
			that sounds like a a great idea to me.")""")