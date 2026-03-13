import pandas as pd
import requests
from io import StringIO

# =====================
# SYMBOL MAP
# =====================

SYMBOL_MAP = {
    "crudeoil": "cl.f"
}

# =====================
# DATA DOWNLOAD
# =====================

def get_data(asset):

    try:

        symbol = SYMBOL_MAP[asset]

        url = f"https://stooq.com/q/d/l/?s={symbol}&i=5"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        df = pd.read_csv(StringIO(response.text))

        if df.empty:
            return None

        df.columns = [
            "date",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]

        # prendiamo le ultime 200 candele
        df = df.tail(200)

        return df

    except Exception as e:

        print("Data error:", e)

        return None
