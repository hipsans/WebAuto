import time
from selenium import webdriver
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet("Playlist")
ws.append(["Title", "Hashtag", "Like#", "Song#"])

driver = webdriver.Chrome("../chromedriver")
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/music")

# driver.execute_script("window.scrollTo(0,200);")
# scrollHeight = driver.execute_script("return document.body.scrollHeight")
#
# print(scrollHeight)

#현재 scrollHeight가져오기
lastHeight = driver.execute_script("return document.body.scrollHeight")
print(lastHeight)

while True:
    #scrollHeight[lastHeight]까지 스크롤
    driver.execute_script("window.scrollTo(0, "+ str(lastHeight) +")")

    #새로운 내용 로딩될때까지 기다림
    time.sleep(1)

    #새로운 내용 로딩됐는지 확인
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

playlists = driver.find_elements_by_css_selector("div.playlist__meta")

for playlist in playlists:
    title = playlist.find_element_by_css_selector("h3.title").text
    hashtags = playlist.find_element_by_css_selector("p.tags").text
    like_count = playlist.find_element_by_css_selector("span.data__like-count").text
    music_count = playlist.find_element_by_css_selector("span.data__music-count").text

    ws.append([title, hashtags, like_count, music_count])

driver.quit()
wb.save("PlaylistINFO.xlsx")