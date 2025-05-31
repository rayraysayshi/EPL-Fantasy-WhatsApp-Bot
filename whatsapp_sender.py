# whatsapp_sender.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import WHATSAPP_GROUP_NAME

def send_message_via_whatsapp(message):
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    input("Scan QR and press Enter...")

    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(WHATSAPP_GROUP_NAME)
    time.sleep(2)

    group = driver.find_element(By.XPATH, f'//span[@title="{WHATSAPP_GROUP_NAME}"]')
    group.click()
    time.sleep(1)

    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.send_keys(message)
    time.sleep(1)

    send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_button.click()

    time.sleep(5)
    driver.quit()