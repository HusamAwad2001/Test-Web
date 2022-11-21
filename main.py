from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://hussamawad.000webhostapp.com/contact/")

firstName = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "wpforms[fields][0][first]")))
firstName.send_keys("Husam")

lastName = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "wpforms[fields][0][last]")))
lastName.send_keys("Dahliz")

email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "wpforms[fields][1]")))
email.send_keys("husam@gmail.com")

message = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "wpforms[fields][2]")))
message.send_keys("Hello World!")

create = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "wpforms[submit]")))
create.click()