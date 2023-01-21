import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from PIL import Image
from pyzbar.pyzbar import decode
import io
import time

DRIVERS = {
    "chrome": (lambda: wd.Chrome()),
    "firefox": (lambda: wd.Firefox()),
    "safari": (lambda: wd.Safari()),
    "edge": (lambda: wd.Edge())
}

def create_driver(brosware_name:str) -> wd.Chrome:
    driver = DRIVERS[brosware_name.lower()]()
    return driver


def get_qrimage(driver):
    time.sleep(2)
    element = driver.find_elements(By.CLASS_NAME,"bigger-qr-code")
    qrcode  = Image.open(io.BytesIO(element[0].screenshot_as_png))
    data = decode(qrcode)
    if data:
        data = data[0]
        qrcode = qrcode.crop((data.rect.left,
                                data.rect.top,
                                data.rect.width+data.rect.left,
                                data.rect.height+data.rect.top))
        return qrcode,data.data
    return None,None
