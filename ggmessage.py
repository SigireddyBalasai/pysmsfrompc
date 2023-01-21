from utils import get_qrimage,create_driver

def recall_qrcode(broswer:str = "Chrome"):
    driver = create_driver(broswer)
    driver.get("https://messages.google.com/web/authentication")
    qrcode,data = get_qrimage(driver)
    if qrcode is not None:
        qrcode.save("qrcode.png")
        print(data)


