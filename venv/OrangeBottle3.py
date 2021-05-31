import csv
import requests
from bs4 import BeautifulSoup

csv_file = open("OB3.csv", "w")
csv_writer = csv.writer(csv_file)

#Header
csv_writer.writerow(["Branch", "Address", "PhoneNumber"])

page = requests.get("https://workey.codeit.kr/orangebottle/index")
pageCode = page.text
soup = BeautifulSoup(pageCode, "html.parser")

branchInfo = soup.select(".container .branch")

for line in branchInfo[0:]:
    row = [
        line.select_one(".city").get_text(),
        line.select_one(".address").get_text(),
        line.select_one(".phoneNum").get_text()
    ]
    csv_writer.writerow(row)

csv_file.close()

