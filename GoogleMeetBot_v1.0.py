from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


class ZoomBot:

    def __init__(self, username, password, key1):
        self.username = username
        self.password = password
        self.key1 = key1
        options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://stackoverflow.com/users/login')
        time.sleep(1)
        google = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="openid-buttons"]/button[1]')))
        google.click()
        time.sleep(1)

        email = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']")))
        email.send_keys(username)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        pyautogui.write(password, interval=0.05)
        pyautogui.press('enter')
        time.sleep(3)
    def login(self):
        driver = self.driver
        try:
            driver.get("https://meet.google.com")

            keys = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i2')))
            keys.click()
            keys.send_keys(key1)
            keys.send_keys(Keys.ENTER)
        except:
            self.login()



username = '' #Your Email Here
password = '' #your Password Here
key1 = '' # Your Key here
try:
    zoom1 = ZoomBot(username, password, key1)
    zoom1.login()
except:
    zoom1 = ZoomBot(username, password, key1)
    zoom1.login()
