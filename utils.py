import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from PIL import Image,ImageOps
from pyzbar.pyzbar import decode
import io
import time

DRIVERS = {
    "chrome": (lambda options: wd.Chrome(options=options)),
    "firefox": (lambda options: wd.Firefox(options=options)),
    "safari": (lambda options: wd.Safari(options=options)),
    "edge": (lambda options: wd.Edge(options=options))
}

#Options headless broswer
CHROMEOPTIONS = wd.ChromeOptions()
CHROMEOPTIONS.headless=True
FIREFOXOPTIONS = wd.FirefoxOptions()
FIREFOXOPTIONS.headless = True
SAFARIOPTIONS = wd.FirefoxOptions()
SAFARIOPTIONS.headless = True
EDGEOPTIONS = wd.EdgeOptions()
EDGEOPTIONS.headless = True

OPTIONS ={
	"chrome":CHROMEOPTIONS,
	"firefox": FIREFOXOPTIONS,
    "safari": SAFARIOPTIONS,
    "edge": EDGEOPTIONS,
	"headyes": None
}

# Custom Exceptions

class BrowserException(Exception):
	def __init__(self):
		super(BrowserException,self).__init__("Only [Chrome, Firefox, Safari, Edge] are supported")	

class TimeOutConnectionException(Exception):
	def __init__(self):
		super(TimeOutConnectionException,self).__init__("Verify your internet connection")		

# functions

def create_driver(brosware_name:str,open_head:bool) -> wd.Chrome:
	try:
		if not open_head:
			driver = DRIVERS[brosware_name.lower()](options = OPTIONS[brosware_name.lower()])
			return driver
		driver = DRIVERS[brosware_name.lower()](options = OPTIONS["headyes"])
	except KeyError as e:
		raise(BrowserException())
	return driver


def get_qrimage(driver:wd.Chrome) -> list([Image,bytes]):
	'''
		The function return the qrcode image in PIL format and \n
		the bytes massege inside the qr code
	'''
	element, start = [], time.time()
	while len(element) == 0:
		element = driver.find_elements(By.CLASS_NAME,"bigger-qr-code")
		if time.time() - start > 10:
			raise TimeOutConnectionException()
	qrcode  = Image.open(io.BytesIO(element[0].screenshot_as_png))
	data = decode(qrcode)
	if data:
		data = data[0]
		qrcode = qrcode.crop((data.rect.left,
								data.rect.top,
								data.rect.width+data.rect.left,
								data.rect.height+data.rect.top))
		qrcode = ImageOps.equalize(ImageOps.grayscale(qrcode))
		qrcode = ImageOps.expand(qrcode,border=50,fill="white")
		return qrcode,data.data
	return None,None
