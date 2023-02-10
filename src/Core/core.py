import selenium.webdriver as wd
from selenium.webdriver.common.by import By
import time
from .exceptions import *
import os

DRIVERS = {
    "chrome": (lambda options: wd.Chrome(options=options)),
    "firefox": (lambda options: wd.Firefox(options=options)),
    "safari": (lambda options: wd.Safari(options=options)),
    "edge": (lambda options: wd.Edge(options=options))
}

#Options headless broswer
CHROMEOPTIONS = wd.ChromeOptions()
CHROMEOPTIONS.headless=True
# CHROMEOPTIONS.add_experimental_option("debuggerAddres","localhost:8989")
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

# functions

def create_driver(brosware_name:str,headless:bool) -> wd.Chrome:
	try:
		if headless:
			driver = DRIVERS[brosware_name.lower()](options = OPTIONS[brosware_name.lower()])
			return driver
		driver = DRIVERS[brosware_name.lower()](options = OPTIONS["headyes"])
	except KeyError as e:
		raise(BrowserException())
	return driver

def click_to_send(driver: wd.Chrome) -> bool:
	try:
		send_button = driver.find_elements(By.CSS_SELECTOR,"[data-e2e-send-text-button]")
		for button in send_button:
			if button.aria_role == "button":
				button.click()
		return True
	except:
		return False

def get_qrlogin(driver:wd.Chrome,keep_logged) -> bool:
	'''
		The function return the qrcode image in PIL format and \n
		the bytes massege inside the qr code
	'''
	element, start = [], time.time()
	while len(element) == 0:
		element = driver.find_elements(By.CLASS_NAME,"bigger-qr-code")
		if time.time() - start > 10:
			raise TimeOutConnectionException()
	if keep_logged:
		button = driver.find_element(By.ID,"mat-mdc-slide-toggle-1-button").click()
	while not "conversations" in driver.current_url:
		time.sleep(0.5)
	return True

def select_chat(driver:wd.Chrome,number:str) -> bool:
	input_number= []
	start = time.time()
	while len(input_number) == 0:
		input_number = driver.find_elements(By.CLASS_NAME,"input")
		if time.time() - start > 10:
			raise TimeOutConnectionException()
	input_number[0].send_keys(number)
	button = driver.find_elements(By.CLASS_NAME,"button")
	isclicked = False
	while not isclicked:
		#TODO: how to better handle this
		try:
			button[0].click()
			isclicked = True
		except:
			pass
	return True

def send_message_to(driver:wd.Chrome,number:str,message:str) -> bool:
	
	state = select_chat(driver,number)
	input_message = []
	start = time.time()
	while len(input_message) == 0:
		input_message = driver.find_elements(By.CLASS_NAME,"input-box")
		if time.time() - start > 10:
			raise TimeOutConnectionException()
	input_message = input_message[0].find_elements(By.CLASS_NAME,"input")
	input_message[1].send_keys(message)
	time.sleep(1)
	state = click_to_send(driver)
	return state

def send_hattacment_to(driver:wd.Chrome,number:str,path:str)-> bool:
	
	state = select_chat(driver,number)
	
	input_attachment = []
	start = time.time()
	while len(input_attachment) == 0:
		input_attachment = driver.find_elements(By.CSS_SELECTOR,"[data-e2e-picker-button=ATTACHMENT]")
		if time.time() - start > 10:
			raise TimeOutConnectionException()
	time.sleep(3)
	#TODO:
	# implement the execution of uploading
	time.sleep(1)
	state = click_to_send()
	return state


	

