import pandas as pd
import yfinance as yf
from src.algorithm import rsi

# These are the dates on which I would have bought the stock
ticker_dates = {
  "INFY.NS": ["11-09-2017", 
              "11-04-2018", 
              "26-10-2018", 
              "22-11-2018",
              "22-10-2019",
              "19-03-2020",
              "03-09-2020",
              "30-10-2020",
              "12-05-2021",
              "02-03-2022"],
}

all_data = pd.DataFrame()

for ticker in ticker_dates.keys():
    # Download the data for the ticker
    start_date = pd.to_datetime(ticker_dates[ticker][0], format="%d-%m-%Y") - pd.DateOffset(months=1)
    end_date = pd.to_datetime(ticker_dates[ticker][-1], format="%d-%m-%Y") + pd.DateOffset(months=1)
    print("Downloading data for {} from {} to {}".format(ticker, start_date, end_date))
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Add rsi column
    stock_data['rsi21'] = rsi.calculate(stock_data['Close'], 21)

    # Add column for exponential moving average
    stock_data['ema21'] = stock_data['Close'].ewm(span=21, adjust=False).mean()
    stock_data['ema7'] = stock_data['Close'].ewm(span=7, adjust=False).mean()

    # Add column for last 7 days average volume
    stock_data['volume7'] = stock_data['Volume'].rolling(window=7).mean()

    # Add 7 colums for past 7 days
    for i in range(1, 8):
        stock_data['day{}'.format(i)] = stock_data['Close'].shift(i)

    # Add a column 'buy' and set it to 0
    stock_data['Date'] = stock_data.index
    stock_data['buy'] = 0
    
    # Convert the dates in ticker_dates to yyyy-mm-dd format
    ticker_dates_yyyymmdd = [pd.to_datetime(date, format="%d-%m-%Y").strftime("%Y-%m-%d") for date in ticker_dates[ticker]]
    
    for date in ticker_dates_yyyymmdd:
        stock_data.loc[stock_data['Date'] == date, 'buy'] = 1
    
    all_data = all_data._append(stock_data)

    # Save
    stock_data.to_csv("data/{}.csv".format(ticker))

# Sort the DataFrame by date
all_data.sort_index(inplace=True)

# Print the resulting DataFrame with the 'buy' column
print(all_data)
