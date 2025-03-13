from selenium import webdriver
from selenium.webdriver.common.by import By

browers = ["Chrome","Firefox"]

for brower in browers:
    if brower == "Chrome":
      driver = webdriver.Chrome()
    elif brower == "Firefox":
      driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")
    print(f"running test on {brower}")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login = driver.find_element(By.ID, "login-button")
    login.click()

    print("Login Successful!")
    driver.quit()
