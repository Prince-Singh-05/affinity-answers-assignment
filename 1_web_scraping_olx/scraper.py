from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import time

url = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, timeout=60000)

    time.sleep(4)

    # Keep loading until no load more
    while True:
        # Scroll to bottom
        page.mouse.wheel(0, 5000)
        time.sleep(2)

        # Try clicking Load More button
        try:
            load_more = page.locator('button[data-aut-id="btnLoadMore"]')
            if load_more:
                print("Clicking Load More...")
                load_more.click()
                time.sleep(3)
            else:
                print("No more Load More button; exiting scroll loop.")
                break
        except:
            print("Load More not found; stopping.")
            break

    # Get final HTML content
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    # Correct selector for items on olx
    items = soup.select('li[data-aut-id="itemBox3"]')
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

    browser.close()
