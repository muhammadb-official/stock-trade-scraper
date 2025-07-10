import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_openinsider():
    url = "http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=90&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="tinytable")
    rows = table.find_all("tr")[1:]

    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 9:
            continue
        try:
            date = cols[2].text.strip()
            ticker = cols[4].text.strip()
            insider = cols[5].text.strip()
            transaction = cols[6].text.strip()
            qty = int(cols[7].text.strip().replace(",", ""))
            price = float(cols[8].text.strip().replace("$", "").replace(",", ""))
            total = qty * price
            link = url
            data.append({
                "Category": "Insider",
                "Filer Name": insider,
                "Date": date,
                "Ticker": ticker,
                "Transaction Type": transaction,
                "Quantity": qty,
                "Price": price,
                "Total Value": total,
                "Source URL": link
            })
        except:
            continue

    return pd.DataFrame(data)
