import pandas as pd
import numpy as np

def calculate(data, time_window):
  avg = data.rolling(window=time_window).mean()
  return avg