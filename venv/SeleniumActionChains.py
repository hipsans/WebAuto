import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("../chromedriver")
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/costagram/index")

driver.find_element_by_css_selector(".top-nav__login-link").click()
time.sleep(1)

id_box = driver.find_element_by_css_selector(".login-container__login-input")
pw_box = driver.find_element_by_css_selector(".login-container__password-input")
login_button = driver.find_element_by_css_selector(".login-container__login-button")

# (ActionChains(driver)
#     .send_keys_to_element(id_box, "codeit")
#     .send_keys_to_element(pw_box, "datascience")
#     .click(login_button)
#     .perform())

actions = ActionChains(driver)
actions.send_keys_to_element(id_box, "codeit")
actions.send_keys_to_element(pw_box, "datascience")
actions.click(login_button)
actions.perform()


