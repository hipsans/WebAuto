import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text
soupedPage = BeautifulSoup(rating_page, "html.parser")
programTitleTags = soupedPage.select("td.program")

print(programTitleTags)