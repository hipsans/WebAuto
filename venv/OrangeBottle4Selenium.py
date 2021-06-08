from selenium import webdriver

driver = webdriver.Chrome("../chromedriver")
driver.get("https://workey.codeit.kr/orangebottle/index")

branch_info = []

for branch in driver.find_elements_by_css_selector("div.branch"):
    name = branch.find_element_by_class_name("city").text
    address = branch.find_element_by_class_name("address").text
    phNumber = branch.find_element_by_class_name("phoneNum").text
    branch_info.append([name, address, phNumber])

print(branch_info)

driver.quit()