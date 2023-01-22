from utils import get_qrlogin,create_driver,send_message_to
from selenium.webdriver.support.wait import WebDriverWait

def login(broswer:str = "Chrome",headless:bool =True,keep_logged = False) -> None:
    '''
    #Input:
    - broswer: select your broswer from [chrome, firefox, edge, safari]
    - headless: if False the broswer page is opened
    - keep_logged: if True save the login for the browser
    '''
    driver = create_driver(broswer,headless)
    driver.get("https://messages.google.com/web/authentication")
    state = get_qrlogin(driver,keep_logged)
    if not state:
        driver.quit()
        return None
    return driver

def send_message(broswer:str = "Chrome",
                 headless:bool =True,
                 number:str = None,
                 message:str = None,
                 driver = None):
    if driver is None:
        driver = create_driver(broswer,headless)
    driver.get("https://messages.google.com/web/conversations/new")
    state = send_message_to(driver,number,message)
    if state:
        print("Messaggio inviato correttamente")
    


