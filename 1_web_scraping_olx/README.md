## Problem Statement - OLX Scraper

I am searching for a “Car Cover” on OLX - using this URL https://www.olx.in/items/q-car-cover?isSearchCall=true; I need a python program that gives me the search results parameters - like title of the ad, description and price. Print the results in table format. Don’t bother about the image. Place the code in Github and share the link.

## Features

- Uses Playwright to load JavaScript-rendered pages (OLX blocks direct HTTP requests).
- Scrapes listings using BeautifulSoup for reliable HTML parsing.
- Fully automated browser workflow.
- Works on any OLX search URL.
- Easily extendable for more data fields (price, location, link, images, etc.)

## Installation

1. Clone the repository

   ```
   git clone https://github.com/your-username/olx-scraper.git
   cd olx-scraper
   ```

2. Create a virtual environment

   ```
   python3 -m venv olx-scraper-vevn
   source olx-scraper-venv/bin/activate         # macOS / Linux
   olx-scraper-venv\Scripts\activate            # Windows (Command Prompt)
   .\olx-scraper-venv\Scripts\Activate.ps1      # Windows (PowerShell)
   ```

3. Install dependencies

   ```
   pip install -r requirements.txt
   ```

4. Install Playwright browsers

   ```
   playwright install
   ```

5. Run the scraper
   ```
   python3 ./scraper.py
   ```
