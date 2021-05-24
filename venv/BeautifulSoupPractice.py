import requests
from bs4 import BeautifulSoup

#requests.get을 사용하여 싸이트 코드 받기; 객체로 받고, 객체.text로 코드를 빼낸다.
response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

#아마도 BeautifulSoup으로 html태그 인식한 객체로 코드처리 후, 선택자로 특정 코드 추출
#추출된 코드는 객체리스트로 반환, 리스트 멤버들은 객체이기에 select메서드 사용 가능.
soupedPage = BeautifulSoup(rating_page, "html.parser")
tr_tag = soupedPage.select("tr")[1]
td_tags = tr_tag.select("td")

for tag in td_tags:
    print(tag.get_text())

# print(soupedPage.select("tr")[1])


# programTitleTags = soupedPage.select("td")
# td_tags = programTitleTags[:4]
# for tag in td_tags:
#     print(tag.get_text())
