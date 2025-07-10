from scrapers.openinsider import scrape_openinsider
from scrapers.housestockwatcher import scrape_congress
import pandas as pd
from datetime import datetime
import os

def main():
    os.makedirs("data", exist_ok=True)

    # Run scrapers
    insider_df = scrape_openinsider()
    congress_df = scrape_congress()

    # Combine datasets
    combined_df = pd.concat([insider_df, congress_df], ignore_index=True)
    combined_df["Data Timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Save to CSV
    combined_df.to_csv("data/trades.csv", index=False)
    print("✅ Data saved to data/trades.csv")

if __name__ == "__main__":
    main()
