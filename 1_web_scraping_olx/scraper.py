import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

URL = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Starting scraper...")

res = requests.get(URL, headers=headers)
print("response code - ", res.status_code)

soup = BeautifulSoup(res.text, "html.parser")

items = soup.select('li[data-aut-id="itemBox3"]')  # class used for listings
print("Total items found:", len(items))

table = PrettyTable(["Title", "Price", "Location"])

for item in items:
    title = item.select_one('span[data-aut-id="itemTitle"]')
    price = item.select_one('span[data-aut-id="itemPrice"]')
    location = item.select_one('span[data-aut-id="item-location"]')

    table.add_row([
        title.get_text(strip=True) if title else "N/A",
        price.get_text(strip=True) if price else "N/A",
        location.get_text(strip=True) if location else "N/A",
    ])

print(table)
