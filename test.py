from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

time.sleep(2)

user_name=driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")

password_field =driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(5)

driver.quit()