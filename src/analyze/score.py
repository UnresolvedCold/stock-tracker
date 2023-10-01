from src.algorithm import rsi

def calculate_score(stock_data):
  rsi_series = rsi.calculate(stock_data['Close'], 17)
  rsidf = rsi_series.to_frame("rsi")
  # exponential moving average of rsi
  rsidf['ema'] = rsidf['rsi'].ewm(span=17, adjust=False).mean()
  print(rsidf.tail())

  if rsidf['ema'].iloc[-1] > 40 and rsidf['rsi'].iloc[-1] < 30:
    return rsidf['rsi'].iloc[-1]
  if rsidf['ema'].iloc[-1] > 60 and rsidf['rsi'].iloc[-1] < 50:
    return rsidf['rsi'].iloc[-1]
  else:
    return 100
