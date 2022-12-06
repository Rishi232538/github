from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")
Action = ActionChains(driver)

MouseHover = driver.find_element(By.CSS_SELECTOR, "button#mousehover")
Action.move_to_element(MouseHover).perform()

driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[1]").click()