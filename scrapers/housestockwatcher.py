import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

def scrape_congress():
    base_url = "https://housestockwatcher.com/trades"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    table = soup.find("table")
    rows = table.find_all("tr")[1:]  # skip header

    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 6:
            continue
        try:
            name = cols[0].text.strip()
            ticker = cols[2].text.strip()
            action = cols[3].text.strip()
            transaction_date = cols[4].text.strip()
            amount = cols[5].text.strip()
            amount = amount.replace("$", "").replace(",", "").replace("+", "")
            amount = amount.split(" - ")[-1]  # Use upper bound for estimate

            est_amount = float(amount) if amount.isdigit() else None
            price = est_amount  # no per-share price, so use estimate
            quantity = "N/A"

            data.append({
                "Category": "Congress",
                "Filer Name": name,
                "Date": transaction_date,
                "Ticker": ticker,
                "Transaction Type": action,
                "Quantity": quantity,
                "Price": "N/A",
                "Total Value": est_amount,
                "Source URL": base_url
            })
        except Exception as e:
            continue

    return pd.DataFrame(data)
