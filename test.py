from ideabox_app import app 
import unittest


class FlaskTestCase(unittest.TestCase):

	# Ensures that Flask is correctly set up
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type="html/text")
		self.assertEqual(response.status_code, 200)

	# Ensures that login page loads correctly
	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type="html/text")
		self.assertTrue(b'Please login' in response.data)

	# Ensures that login behaves correctly with the correct given credentials
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b"login successful", response.data)


	# Ensures that login behaves correctly with the inccorrect given credentials
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="wrong", password="wrong"),
			follow_redirects=True
		)
		self.assertIn(b"Invalid login", response.data)

	# Ensures that logout behaves correctly 
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
		)
		response.tester.get('/logout', follow_redirects=True)
		self.assertIn(b"You are logged out", response.data)

	# Ensures that index page requires a login
	def test_main_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertTrue(b'You need to login first' in response.data)

	# Ensures that our post appears on the index page
	def test_post_show_up(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b"Jump out of the earth", response.data)


if __name__ == '__main__':
	unittest.main()