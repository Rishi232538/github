import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
path = Service("C:/Users/Rishi Ramanathan/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=path)

driver.maximize_window()

#*************************************************************************

driver.implicitly_wait(14)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("br")

increment = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div[2]/a[2]")

driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[1]/div[3]/button").click()

driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[3]/button").click()

driver.find_element(By.XPATH, "//a[@class='cart-icon']/img").click()

driver.find_element(By.XPATH, "//*[text()='PROCEED TO CHECKOUT']").click()

Price1 = driver.find_element(By.XPATH, "//*[@id='productCartTables']/tbody/tr[1]/td[5]/p")
PriceA = int(Price1.text)
print(PriceA)

Price2 = driver.find_element(By.XPATH, "//*[@id='productCartTables']/tbody/tr[2]/td[5]/p")
PriceB = int(Price2.text)
print(PriceB)

ActualPrice = PriceA + PriceB
print(ActualPrice)

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

ExpectedPrice = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/span[1]")
PriceC = int(ExpectedPrice.text)
print(PriceC)












