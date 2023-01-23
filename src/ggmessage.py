from .Core.core import get_qrlogin,create_driver,send_message_to,send_hattacment_to
import time

def login(broswer:str = "Chrome",headless:bool =True,keep_logged = True) -> None:
    '''
    #Input:
    - broswer: select your broswer from [chrome, firefox, edge, safari]
    - headless: if False the broswer page is opened
    - keep_logged: if True save the login for the current browser session
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
                 driver = None)-> None:

    if driver is None:
        driver = login(broswer,headless)
    driver.get("https://messages.google.com/web/conversations/new")
    state = send_message_to(driver,number,message)
    if state:
        print("Message sent correctly")

def send_attachment_message(broswer:str = "Chrome",
                 headless:bool =True,
                 number:str = None,
                 path:str = None,
                 driver = None) -> None:

    if driver is None:
        driver = login(broswer,headless)
    while not "conversations" in driver.current_url:
        time.sleep(2)
    driver.get("https://messages.google.com/web/conversations/new")
    state = send_hattacment_to(driver,number,path)
    if state:
        print("Attachment sent correctly")


