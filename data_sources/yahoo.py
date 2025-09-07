# /data_sources/yahoo.py
import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime

def fetch_yahoo(ticker="SPY", period="1y", interval="1d"):
    """
    Fetch historical market data from Yahoo Finance and save as CSV
    """
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)

    Path("data/raw/yahoo").mkdir(parents=True, exist_ok=True)

    file_path = f"data/raw/yahoo/{ticker}_{datetime.today().strftime('%Y-%m-%d')}.csv"
    df.to_csv(file_path, index=False)

    print(f"Saved {ticker} data to {file_path}")
    return file_path
