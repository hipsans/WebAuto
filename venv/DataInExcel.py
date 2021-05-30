import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet("TV Ratings")
ws.append(["Ranking", "Channel", "Program", "Rate"])


page = requests.get("https://workey.codeit.kr/ratings/index")
pageText = page.text
soup = BeautifulSoup(pageText, "html.parser")
for tr_tag in soup.select("tr")[1:]:
    td_tag = tr_tag.select("td")
    tableRow = [
        td_tag[0].get_text(),
        td_tag[1].get_text(),
        td_tag[2].get_text(),
        td_tag[3].get_text()
    ]
    ws.append(tableRow)

wb.save("ViewRating2010_01_FIR.xlsx")

