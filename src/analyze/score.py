from src.algorithm import rsi

def calculate_score(stock_data):
  rsidf = rsi.calculate(stock_data['Close'], 21)
  return rsidf.iloc[-1]