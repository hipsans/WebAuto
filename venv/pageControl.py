import time
from selenium import webdriver

driver = webdriver.Chrome("../chromedriver")
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/costagram/index")

# driver.find_element_by_css_selector(".top-nav__login-link").click()
# driver.find_element_by_css_selector(".login-container__login-input").send_keys("codeit")
# driver.find_element_by_css_selector(".login-container__password-input").send_keys("datascience")
# driver.find_element_by_css_selector(".login-container__login-button").click()
time.sleep(1)
#크롬 개발자 도구 사용 선택자 가져오기
driver.find_element_by_css_selector("#app > nav > div > a").click()
time.sleep(1)
driver.find_element_by_css_selector("#app > div > div > div > form > input.login-container__login-input").send_keys("codeit")
driver.find_element_by_css_selector("#app > div > div > div > form > input.login-container__password-input").send_keys("datascience")
driver.find_element_by_css_selector("#app > div > div > div > form > input.login-container__login-button").click()


