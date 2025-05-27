import logging
import time
import numpy as np
from datetime import datetime
from utils  import storage, calc, time as time_util  # Import the time utility

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_daily():
    ticker = 'LCID'
    recent_csv_file = 'recent_stock_data.csv'
    historical_csv_file = 'historical_stock_data.csv'
    window_size = 30  # For the recent data window

    # Load current stock data from the CSV file
    stock_data = storage.load_or_initialize_csv(recent_csv_file)

    # Update the stock data with the latest price only if it's trading time
    if time_util.is_trading_time():
        stock_data = storage.update_csv(stock_data, recent_csv_file, historical_csv_file, ticker, window_size)

        # If there's enough historical data, we proceed to calculate and predict local minima/maxima
        if len(stock_data) > window_size:
            x = range(len(stock_data))  # Indices as x-values
            y = stock_data['Price'].values  # Prices as y-values

            # Fit a polynomial regression model to the data
            degree = 3  # Degree of the polynomial
            coeffs, p, mse = calc.fit_and_evaluate(x, y, degree)
            
            # Compute derivatives (slopes) to find local minima and maxima
            dp = np.polyder(p)
            d2p = np.polyder(dp)
            
            # Find local minima/maxima
            extrema = calc.find_extrema(p, dp, d2p, min(x), max(x))

            # Check if we need to buy, sell, or hold based on extrema
            for x_extremum, y_extremum, extremum_type in extrema:
                if extremum_type == "Minimum":
                    # If local minimum and price is in lower 25%, buy
                    if y_extremum < min(y) + 0.25 * (max(y) - min(y)):
                        logging.info(f"Action: BUY at {y_extremum} - Local minimum detected.")
                        # Call a function to execute the buy action here
                elif extremum_type == "Maximum":
                    # If local maximum and price has increased by 20%, sell
                    if y_extremum > max(y) * 1.2:
                        logging.info(f"Action: SELL at {y_extremum} - Local maximum detected.")
                        # Call a function to execute the sell action here
                else:
                    logging.info(f"Action: HOLD at {y_extremum} - Inflection point detected.")
    else:
        logging.info("Not trading time. Skipping update.")

def main():
    while True:
        # Check if the current time is 9:30 AM to run the script once a day
        now = datetime.now()
        if now.hour == 9 and now.minute == 30:
            logging.info("Starting daily run at 9:30 AM.")
            run_daily()
            time.sleep(86400)  # Sleep for 24 hours before running again
        else:
            logging.info(f"Not the right time. Current time: {now.hour}:{now.minute}")
            time.sleep(60)  # Sleep for 1 minute before checking the time again

# Run the script continuously, but it will only perform updates once a day at 9:30 AM
main()
