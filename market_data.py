import yfinance as yf
import pandas as pd

def get_data(asset):

    try:

        ticker = "CL=F"

        # timeframe principale
        data_5m = yf.download(
            ticker,
            period="1d",
            interval="5m",
            progress=False
        )

        # timeframe trend
        data_1h = yf.download(
            ticker,
            period="5d",
            interval="1h",
            progress=False
        )

        if data_5m.empty or data_1h.empty:
            return None, None

        data_5m = data_5m.reset_index()
        data_1h = data_1h.reset_index()

        df5 = pd.DataFrame()
        df1 = pd.DataFrame()

        df5["date"] = data_5m["Datetime"]
        df5["open"] = data_5m["Open"]
        df5["high"] = data_5m["High"]
        df5["low"] = data_5m["Low"]
        df5["close"] = data_5m["Close"]
        df5["volume"] = data_5m["Volume"]

        df1["date"] = data_1h["Datetime"]
        df1["open"] = data_1h["Open"]
        df1["high"] = data_1h["High"]
        df1["low"] = data_1h["Low"]
        df1["close"] = data_1h["Close"]
        df1["volume"] = data_1h["Volume"]

        return df5.tail(200), df1.tail(200)

    except Exception as e:

        print("Data error:", e)

        return None, None
    except Exception as e:

        print("Data error:", e)

        return None
