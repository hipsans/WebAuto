import time
import requests
from selenium import webdriver
from openpyxl import Workbook

#Creating Excel File
wb = Workbook(write_only=True)
ws = wb.create_sheet("CostagramScraping")
ws.append(["Img Address", "Contents", "Hashtags", "Like Count", "Reply Count"])

#드라이버 생성후 페이지 접속
driver = webdriver.Chrome("../chromedriver")
driver.get("https://workey.codeit.kr/costagram/index")
driver.implicitly_wait(5)

#로그인
driver.find_element_by_css_selector(".top-nav__login-link").click()
driver.find_element_by_css_selector(".login-container__login-input").send_keys("codeit")
driver.find_element_by_css_selector(".login-container__password-input").send_keys("datascience")
driver.find_element_by_css_selector(".login-container__login-button").click()

#페이지 끝까지 스크롤하여 HTML코드 펼치기
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, "+ str(lastHeight) +")")
    time.sleep(3)
    print(lastHeight)
    #새로운 내용이 로딩되었는지 확인
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if lastHeight == newHeight:
        break
    else:
        lastHeight = newHeight

#각 포스팅 클릭, 이미지 주소 저장, 닫기 버튼 누르기
postlist = driver.find_elements_by_css_selector(".post-list__post")

# imgList = []
for post in postlist:
    post.click()
    time.sleep(2)
    #이미지 주소 구하기
    imgPath = driver.find_element_by_css_selector(".post-container__image").get_attribute("style").split('"')[1]
    imgUrl = "https://workey.codeit.kr" + imgPath
    #내용구하기
    content = driver.find_element_by_css_selector(".content__text").text
    #해쉬태그구하기
    hashtag = driver.find_element_by_css_selector(".content__tag-cover").text
    #좋아요, 댓글 수 구하기
    likeCount = driver.find_element_by_css_selector(".content__like-count").text
    replyCount = driver.find_element_by_css_selector(".content__comment-count").text
    #워크쉬트에 행 추가
    ws.append([imgUrl, content, hashtag, likeCount, replyCount])

    # imgList.append(imgUrl)
    driver.find_element_by_css_selector(".close-btn").click()

#image file 저장하
# for i in range(len(imgList)):
#     url = imgList[i]
#     response = requests.get(url)
#     filename = f"image{i}.jpg"
#     with open(filename, "wb+") as f:
#         f.write(response.content)

wb.save("CostagramScraping.xlsx")
driver.quit()