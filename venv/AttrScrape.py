import requests
from bs4 import BeautifulSoup

page = requests.get("https://workey.codeit.kr/ratings/index")
pageText = page.text
soup = BeautifulSoup(pageText, "html.parser")
print(soup.select_one("img")["src"])
