import logging
import time
import requests
import os

api_key = os.getenv("API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_latest_price(ticker):
    """Fetch the latest stock price from Finnhub API."""
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        if 'c' in data:
            latest_price = data['c']  # Current price
            return (time.strftime('%Y-%m-%d %H:%M:%S'), latest_price)
        else:
            logging.error(f"Error fetching data for {ticker}: {data.get('error', 'Unknown error')}")
            return (None, None)
    except requests.RequestException as e:
        logging.error(f"Failed to get ticker '{ticker}' due to: {e}")
        return (None, None)