import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###
page = requests.get("https://workey.codeit.kr/orangebottle/index")
soupedPage = BeautifulSoup(page.text, "html.parser")
branchList = soupedPage.select(".branch")
branch_infos = []
for info in branchList:
    branch_info = info.select("p span")
    branch_name = branch_info[0].get_text()
    address = branch_info[2].get_text()
    phone_number = branch_info[3].get_text()
    # address = info.select(".address")
    # phone_number = info.select(".phoneNum")
    # print(branch_name)
    branch_infos.append([branch_name, address, phone_number])

# 출력 코드
print(branch_infos)