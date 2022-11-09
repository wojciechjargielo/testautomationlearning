# My first automated test to check login and logout on site tester.codersguru.pl
# I used time.sleep for better visualisation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://tester.codersguru.pl/login")
login = driver.find_element(By.ID , "username")
login.send_keys("cotona7089@invodua.com")
time.sleep(1)
password = driver.find_element(By.ID , "password")
password.send_keys("1!2@3#")
time.sleep(1)
driver.find_element(By.ID, "_submit").click()
time.sleep(2)

#going to account settings page directly trough the link
#becouse of diffrent paths of navigation on site with diffrent resolutions
driver.get("https://tester.codersguru.pl/settings")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"button").click()
time.sleep(3)
driver.quit()