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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# In Browser we can use---------------------> window.scrollTo(0,600)
# In Browser we can use---------------------> window.scrollBy(0,600)

#driver.execute_script("window.scrollBy(0,600)")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# How to take SS

driver.get_screenshot_as_file("image.png")