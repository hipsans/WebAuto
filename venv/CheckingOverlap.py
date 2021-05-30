import requests
from bs4 import BeautifulSoup

target = requests.get("https://workey.codeit.kr/music")
targetPage = target.text

soupedPage = BeautifulSoup(targetPage, 'html.parser')

liTag = soupedPage.select_one("ul.popular__order li")
print(liTag.text)

# popularArtists = []
# for tag in soupedPage.select("ul.popular__order li"):
#     popularArtists.append(list(tag.stripped_strings)[1])
#
# print(popularArtists)
