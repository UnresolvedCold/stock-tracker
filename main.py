import yfinance as yf
import datetime
from src.algorithm import rsi 
from src.report import html
from src.analyze import score

def main():
    # get tickers list from tickerlist.txt file
    tickers = []
    rsi_threshold2 = 30
    rsi_threshold1 = 50
    start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")

    extreme_buy = []
    can_buy = []
    stock_data_dict = {}  # To store stock price and RSI value for each ticker

    with open('tickerlist.txt', 'r') as f:
        tickers = f.read().splitlines()

    for ticker in tickers:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        _score = score.calculate_score(stock_data)
        stock_price = stock_data['Close'].iloc[-1]

        stock_data_dict[ticker] = {
            'stock_price': stock_price,
            'score': _score
        }

        if _score < rsi_threshold2:
            extreme_buy.append(ticker)
        elif _score < rsi_threshold1:
            can_buy.append(ticker)

    if len(can_buy) == 0 and len(extreme_buy) == 0:
        print("No ticker to buy")
        return

    print("Extreme Buy: ", extreme_buy)
    print("Can Buy: ", can_buy)
    html.generate(extreme_buy, can_buy, stock_data_dict)

if __name__ == "__main__":
    main()
