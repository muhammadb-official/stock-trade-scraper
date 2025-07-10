from scrapers.openinsider import scrape_openinsider
import pandas as pd
from datetime import datetime
import os

def main():
    os.makedirs("data", exist_ok=True)
    
    insider_df = scrape_openinsider()
    
    insider_df["Data Timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    insider_df.to_csv("data/trades.csv", index=False)
    print("✅ Data saved to data/trades.csv")

if __name__ == "__main__":
    main()
