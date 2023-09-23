import pandas as pd
import numpy as np

def calculate(data, time_window):
    delta = data.diff(1)
    delta = delta.dropna()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)

    avg_gains = gains.rolling(window=time_window).mean()
    avg_losses = losses.rolling(window=time_window).mean()

    rs = avg_gains / avg_losses
    rsi = 100 - (100 / (1 + rs))

    return rsi
