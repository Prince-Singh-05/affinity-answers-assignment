import cloudscraper
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

scraper = cloudscraper.create_scraper()  # handles Cloudflare

print("Starting scrapper...")

try:
    res = scraper.get(url, timeout=10)
    print("res -", res.status_code)
except Exception as e:
    print("Request failed:", e)
    exit()

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
