import csv
import requests
from bs4 import BeautifulSoup

#Creating CSV file
csv_file = open("ViewRating2010_01_FIR.csv", "w")
csv_writer = csv.writer(csv_file)

#Adding the Header
csv_writer.writerow(["Ranking", "Channel", "Program", "Rate"])

targetPage = requests.get("https://workey.codeit.kr/ratings/index")
pageCode = targetPage.text
soup = BeautifulSoup(pageCode, "html.parser")

for tr_tag in soup.select("tr")[1:]:
    td_tag = tr_tag.select("td")
    row = [
        td_tag[0].get_text(),
        td_tag[1].get_text(),
        td_tag[2].get_text(),
        td_tag[3].get_text()
    ]
    csv_writer.writerow(row)

csv_file.close()

