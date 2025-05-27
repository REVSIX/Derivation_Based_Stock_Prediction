from datetime import datetime
import logging
import os
import pandas as pd
from pytz import timezone
from utils import time
from utils import stocks

def update_csv(stock_data, recent_csv_file, historical_csv_file, ticker, window_size):
    """Update both recent and historical CSV files."""
    if not time.is_trading_time():
        logging.info(f"Not trading time. Skipping update at {datetime.now(timezone('US/Eastern'))}")
        return stock_data

    timestamp, price = stocks.fetch_latest_price(ticker)
    
    if price is not None:
        new_data = pd.DataFrame({"Datetime": [timestamp], "Price": [price]})
        
        # Update recent CSV with moving window
        stock_data = pd.concat([stock_data, new_data], ignore_index=True).tail(window_size)
        stock_data.to_csv(recent_csv_file, index=False)
        logging.info(f"Updated recent CSV at {timestamp} with price {price}")
        
        # Append to historical CSV without window constraint
        if os.path.exists(historical_csv_file):
            historical_data = pd.read_csv(historical_csv_file)
        else:
            historical_data = pd.DataFrame(columns=["Datetime", "Price"])
        historical_data = pd.concat([historical_data, new_data], ignore_index=True)
        historical_data.to_csv(historical_csv_file, index=False)
        logging.info(f"Updated historical CSV at {timestamp} with price {price}")
        
    else:
        logging.error(f"Failed to fetch data for ticker {ticker}")

    return stock_data

def get_valid_csv_filename(ticker):
    while True:
        filename = f"{ticker}.csv"
        
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        stock_data_dir = os.path.join(parent_dir, "stock_data_recent")
        full_path = os.path.join(stock_data_dir, filename)
        
        if os.path.isfile(full_path):
            print(f"File found: {full_path}")
            return full_path
        else:
            print(f"File not found: {filename}")
            print("Please try again.")

