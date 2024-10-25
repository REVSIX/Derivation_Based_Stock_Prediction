# Derivation Based Stock Prediction

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Upcoming Features](#upcoming-features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
Derivation Based Stock Prediction is a Python-based application that fetches real-time stock prices and predicts future trends using historical data and advanced mathematical analysis. This project aims to provide users with insights into stock market movements and assist in making informed investment decisions.

## Features
- Fetches real-time stock prices from the Finnhub API.
- Updates price data only during trading hours on trading days.
- Stores historical price data in CSV format for analysis.
- User-friendly interface for entering stock tickers.
- Supports multiple stocks and maintains a moving window of recent prices.
- (Upcoming) Performs regression analysis on historical data.
- (Upcoming) Calculates derivatives for trend analysis.
- (Upcoming) Identifies local maxima and minima using horizontal tangent lines.
- (Upcoming) Analyzes concavity using second derivatives.

## Technologies Used
- **Python**: The primary programming language used for development.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computing and array operations.
- **Matplotlib**: For data visualization and plotting.
- **Scikit-learn**: For machine learning and regression analysis.
- **Requests**: To make API calls to fetch stock prices.
- **Python-dotenv**: For managing environment variables securely.
- **Pytz**: To handle timezone conversions for accurate trading time checks.

## Installation
To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/REVSIX/Derivation_Based_Stock_Prediction.git
   cd Derivation_Based_Stock_Prediction
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Finnhub API key:
   ```
   API_KEY=your_finnhub_api_key_here
   ```

## Usage
To run the application, execute the following command in your terminal:

```bash
python upcomingfile.py  # TODO Replace this with an actual release
```

Follow the prompts to enter a valid stock ticker symbol (e.g., AAPL for Apple Inc.). The application will fetch real-time prices and update a CSV file located in the `stock_data` directory.

## How It Works
1. The application prompts the user for a stock ticker symbol.
2. It checks if it's a valid trading day and within market hours.
3. If valid, it fetches the latest stock price from the Finnhub API.
4. The price data is stored in a CSV file, maintaining a moving window of recent prices.
5. (Upcoming) The application will perform regression analysis on the historical data.
6. (Upcoming) It will calculate derivatives to analyze trends and identify critical points.
7. (Upcoming) Local maxima and minima will be identified using horizontal tangent lines.
8. (Upcoming) Concavity analysis will be performed using second derivatives.

## Upcoming Features
- Regression analysis for trend prediction
- Derivative calculations for identifying critical points
- Identification of local maxima and minima
- Concavity analysis using second derivatives
- Advanced visualization of stock trends and predictions

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or feedback, please reach out to:

- **Raunak Verma**: [raunak@pankul.com](mailto:raunak@pankul.com)
- **GitHub**: [REVSIX on Github](https://github.com/REVSIX)
```
