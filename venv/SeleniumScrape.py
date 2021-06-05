from selenium import webdriver

driver = webdriver.Chrome("../chromedriver")
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/music")

popular_artists = []

for artist in driver.find_elements_by_css_selector("ul.popular__order li"):
    popular_artists.append(artist.text.strip())

print(popular_artists)
