import sqlite3

with sqlite3.connect("members.db") as connection:
	c = connection.cursor()
	c.execute("""
		CREATE TABLE IF NOT EXISTS USERS(
			USERNAME TEXT PRIMARY KEY NOT NULL,
			EMAIL TEXT NOT NULL, 
			PASSWORD TEXT NOT NULL)""")
	c.execute('INSERT INTO USERS (EMAIL, PASSWORD) VALUES("fortune", "admin")')

	c.execute("""CREATE TABLE if not exists ideas(title TEXT, description TEXT)""")
	c.execute('INSERT INTO ideas VALUES("Fridge Making Idea", "Get a big box and paint it white")')
	c.execute('INSERT INTO ideas VALUES("Good Idea", "Dive into the oceans and swim to eternity")')


	
	