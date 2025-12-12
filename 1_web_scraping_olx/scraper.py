from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

url = "https://www.olx.in/items/q-car-cover?isSearchCall=true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, timeout=60000)
    page.wait_for_timeout(5000)

    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    
    items = soup.select("li.EIR5N")
    
    for item in items:
        print(item.text.strip(), "\n---")
    
    browser.close()
