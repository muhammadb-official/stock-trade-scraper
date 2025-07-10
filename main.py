from scrapers.openinsider import scrape_openinsider
from scrapers.housestockwatcher import scrape_congress
from scrapers.sec_edgar import scrape_sec
import pandas as pd
from datetime import datetime

def main():
    oi = scrape_openinsider()
    congress = scrape_congress()
    sec = scrape_sec()

    df = pd.concat([oi, congress, sec], ignore_index=True)
    df["Data Timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    df.to_csv("data/trades.csv", index=False)
    print("✅ Data saved to data/trades.csv")

if __name__ == "__main__":
    main()
