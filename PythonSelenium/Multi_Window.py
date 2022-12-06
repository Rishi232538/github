import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
path = Service("C:/Users/Rishi Ramanathan/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=path)

driver.maximize_window()

# GET THE WINDOW
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

Free_Access = driver.find_element(By.XPATH, "//*[text()='Free Access to InterviewQues/ResumeAssistance/Material']")
Free_Access.click()

WindowHandled = driver.window_handles

driver.switch_to.window(WindowHandled[1])

Email = driver.find_element(By.XPATH, "//*[text()='mentor@rahulshettyacademy.com']")
AnotherEmail = Email.text

driver.switch_to.window(WindowHandled[0])

driver.find_element(By.CSS_SELECTOR, "input#username").send_keys(AnotherEmail)

driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("Rishi")

driver.find_element(By.CSS_SELECTOR, "input#terms").click()

driver.find_element(By.CSS_SELECTOR, "input#signInBtn").click()

