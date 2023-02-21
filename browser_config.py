from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(5)
driver.get('https:google.com')
time.sleep(5)
driver.close()

