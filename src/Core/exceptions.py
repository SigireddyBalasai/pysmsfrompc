# Custom Exceptions

class BrowserException(Exception):
	def __init__(self):
		super(BrowserException,self).__init__("Only [Chrome, Firefox, Safari, Edge] are supported")	

class TimeOutConnectionException(Exception):
	def __init__(self):
		super(TimeOutConnectionException,self).__init__("Verify your internet connection")		
