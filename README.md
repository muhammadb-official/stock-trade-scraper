# Stock Trade Scraper (Insider Trades)

This repo scrapes insider stock trades from [OpenInsider.com](http://openinsider.com) and saves them to a CSV.

## Features
- Insider trades from last 90 days
- Daily automated updates via GitHub Actions
- Output saved in `data/trades.csv`

## To Run Locally
```bash
pip install -r requirements.txt
python main.py
