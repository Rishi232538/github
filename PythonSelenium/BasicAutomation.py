import time

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#path = Service("C:/Users/Rishi Ramanathan/Downloads/geckodriver-v0.32.0-win32/geckodriver.exe")
#driver = webdriver.Firefox(service=path)

#path = Service("C:/Users/Rishi Ramanathan/Downloads/edgedriver_win64/msedgedriver.exe")
#driver = webdriver.Edge(service=path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
path = Service("C:/Users/Rishi Ramanathan/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=path)

# GET THE WINDOW
driver.get("https://rahulshettyacademy.com/")

# GET THE TITLE
Title = driver.title
print(Title)

# WINDOW MAXIMIZE
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# WINDOW BACK
#driver.back()

# WINDOW REFRESH
#driver.refresh()

#Send_Keys
name =driver.find_element(By.XPATH, "(//input[@name='name'])[1]")
name.send_keys("Rishi Ramanathan")

Email = driver.find_element(By.XPATH, "//input[@name='email']")
Email.send_keys("rishiramanathan1998@gmail.com")

Password = driver.find_element(By.CSS_SELECTOR, "input#exampleInputPassword1")
Password.send_keys("Rishi Ramanathan")

# Check Box
CheckBox = driver.find_element(By.CSS_SELECTOR, "input#exampleCheck1")
CheckBox.click()

# Radio Button
RadioButton = driver.find_element(By.CSS_SELECTOR, "input#inlineRadio1")
RadioButton.click()

# Drop Down - First Type
Dropdown = driver.find_element(By.CSS_SELECTOR, "select#exampleFormControlSelect1")
Select= Select(Dropdown)
Select.select_by_visible_text("Female")

# Drop Down - Second Type
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.CSS_SELECTOR, "input#autosuggest").send_keys("ind")
time.sleep(2)

Countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(Countries))

for country in Countries:
    if country.text == "India":
        country.click()

#Get_Attribute
Getattribute = driver.find_element(By.CSS_SELECTOR, "input#autosuggest")
print(Getattribute.get_attribute("value"))













