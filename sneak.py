import webapp2

main_html = """
	<html>
	<head>
	<title>sneak</title>
	</head>
	<body>
	<p>This is the sample project</p>
	</body>
	</html>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(main_html)

app= webapp2.WSGIApplication([('/', MainPage)], debug=True)
