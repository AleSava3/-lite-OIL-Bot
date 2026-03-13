
import pandas as pd
import numpy as np

def ema(series,p):
    return series.ewm(span=p).mean()

def rsi(series,p=14):

    delta = series.diff()

    gain = (delta.where(delta>0,0)).rolling(p).mean()
    loss = (-delta.where(delta<0,0)).rolling(p).mean()

    rs = gain/loss

    return 100-(100/(1+rs))

def atr(df,p=14):

    high_low = df["high"]-df["low"]
    high_close = abs(df["high"]-df["close"].shift())
    low_close = abs(df["low"]-df["close"].shift())

    ranges = pd.concat([high_low,high_close,low_close],axis=1)

    tr = ranges.max(axis=1)

    return tr.rolling(p).mean()
