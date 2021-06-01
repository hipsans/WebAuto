#Importing Selenium
from selenium import webdriver

#Creating CromeDriver
driver = webdriver.Chrome("../chromedriver")

# Opening Targetpage
driver.get("https://codeit.kr")

driver.quit()
