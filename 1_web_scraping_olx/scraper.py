import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

URL = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

items = soup.select("li.EIR5N")  # class used for listings

table = PrettyTable(["Title", "Description", "Price"])

for item in items:
    title = item.select_one("span._2tW1I").get_text(strip=True) if item.select_one("span._2tW1I") else "N/A"
    desc = item.select_one("span._2Tvws").get_text(strip=True) if item.select_one("span._2Tvws") else "N/A"
    price = item.select_one("span._89yzn").get_text(strip=True) if item.select_one("span._89yzn") else "N/A"

    table.add_row([title, desc, price])

print(table)
