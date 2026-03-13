import yfinance as yf
import pandas as pd

def get_data(asset):

    try:

        # Crude Oil Futures
        ticker = "CL=F"

        data = yf.download(
            ticker,
            period="1d",
            interval="5m",
            progress=False
        )

        if data.empty:
            return None

        data = data.reset_index()

        df = pd.DataFrame()

        df["date"] = data["Datetime"]
        df["open"] = data["Open"]
        df["high"] = data["High"]
        df["low"] = data["Low"]
        df["close"] = data["Close"]
        df["volume"] = data["Volume"]

        return df.tail(200)

    except Exception as e:

        print("Data error:", e)

        return None
