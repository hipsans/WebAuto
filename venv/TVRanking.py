import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)

for year in range(2010, 2019):
    ws = wb.create_sheet(f"year {year}")
    ws.append(["Period", "Ranking", "Channel", "Program", "Rate"])

    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = f"https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={weekIndex}"
            response = requests.get(url)
            rating_page = response.text
            soup = BeautifulSoup(rating_page, "html.parser")

            for tr_tag in soup.select("tr")[1:]:
                td_tag = tr_tag.select("td")
                period = f"Year {year} Month {month} Week {weekIndex +1}"
                row = [
                    period,
                    td_tag[0].get_text(),
                    td_tag[1].get_text(),
                    td_tag[2].get_text(),
                    td_tag[3].get_text(),
                ]
                ws.append(row)

wb.save("TVRanking.xlsx")


