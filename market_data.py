import pandas as pd
import requests
from io import StringIO

SYMBOL_MAP = {
    "crudeoil": "cl.f"
}

def get_data(asset):

    try:

        symbol = SYMBOL_MAP[asset]

        url = f"https://stooq.com/q/d/l/?s={symbol}&i=5"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            return None

        if not r.text or "html" in r.text.lower():
            return None

        df = pd.read_csv(StringIO(r.text))

        if df.empty:
            return None

        df.columns = ["date","open","high","low","close","volume"]

        return df.tail(200)

    except Exception as e:

        print("Data error:", e)

        return None
