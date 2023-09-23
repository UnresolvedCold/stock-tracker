import yfinance as yf
import pandas as pd
import numpy as np
import datetime

def calculate_rsi(data, time_window):
    delta = data.diff(1)
    delta = delta.dropna()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)

    avg_gains = gains.rolling(window=time_window).mean()
    avg_losses = losses.rolling(window=time_window).mean()

    rs = avg_gains / avg_losses
    rsi = 100 - (100 / (1 + rs))

    return rsi

def moving_average(data, window):
    return data.rolling(window).mean()

def create_html_report(extream_buy, can_buy): 
  html = """<!DOCTYPE html>
  <html>
  <head>
  <style>
  table, th, td {
    border: 1px solid black;
  }
  </style>
  </head>
  <body>
  <h2>Extream Buy</h2>
  <table>
    <tr>
      <th>Ticker</th>
    </tr>"""
  for ticker in extream_buy:
    html += "<tr><td>" + ticker + "</td></tr>"
  html += """</table>
  <h2>Can Buy</h2>
  <table>
    <tr>
      <th>Ticker</th>
    </tr>"""
  for ticker in can_buy:
    html += "<tr><td>" + ticker + "</td></tr>"
  html += """</table>
  </body>
  </html>"""
  with open('report.html', 'w') as f:
    f.write(html)


def main():
  # get tickers list from tickerlist.txt file
  tickers = []
  rsi_threshold2 = 30
  rsi_threshold1 = 50
  start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")
  end_date =  datetime.datetime.now().strftime("%Y-%m-%d")

  extream_buy = []
  can_buy = []

  with open('tickerlist.txt', 'r') as f:
    tickers = f.read().splitlines()
  
  for ticker in tickers:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    rsi = moving_average(stock_data['Close'], 21)
    
    if (rsi.iloc[-1] < rsi_threshold2):
      extream_buy.append(ticker)
    elif (rsi.iloc[-1] < rsi_threshold1):
      can_buy.append(ticker)
  if (len(can_buy) == 0 and len(extream_buy) == 0):
      print("No ticker to buy")
      return
  
  print("Extream Buy: ", extream_buy)
  print("Can Buy: ", can_buy)
  create_html_report(extream_buy, can_buy)

if __name__ == "__main__":
  main()