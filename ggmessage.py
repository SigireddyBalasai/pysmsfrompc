from utils import get_qrimage,create_driver
from selenium.webdriver.support.wait import WebDriverWait

def recall_qrcode(broswer:str = "Chrome",open_head:bool =False) -> None:
    '''
    #Input:
    - broswer: select your broswer from [chrome, firefox, edge, safari]
    - open_head: if True the broswer page is opened
    '''
    driver = create_driver(broswer,open_head)
    driver.get("https://messages.google.com/web/authentication")
    qrcode,data = get_qrimage(driver)
    if qrcode is not None:
        qrcode.save("qrcode.png")
        # driver.get(data.decode('utf-8'))
        # print(data)
    driver.quit()


