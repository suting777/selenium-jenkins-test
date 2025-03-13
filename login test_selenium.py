from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
username.send_keys("standard_user")
password.send_keys("secret_sauce")

login = driver.find_element(By.ID, "login-button")
login.click()

print("Login Successful!")
driver.quit()
