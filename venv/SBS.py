import csv
import requests
from bs4 import BeautifulSoup

csv_file = open("SBS.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Period", "Ranking", "Program", "Rate"])

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            response = requests.get(f"https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={weekIndex}")
            pageCode = response.text
            soup = BeautifulSoup(pageCode, "html.parser")

            for td_tag in soup.select("tr")[1:]:
                if td_tag.select_one(".channel").get_text() == "SBS":
                    period = f"Year {year} Month {month} Week {weekIndex +1}"
                    row = [
                        period,
                        td_tag.select_one(".rank").get_text(),
                        td_tag.select_one(".program").get_text(),
                        td_tag.select_one(".percent").get_text(),
                    ]
                    csv_writer.writerow(row)
                else:
                    pass

csv_file.close()
