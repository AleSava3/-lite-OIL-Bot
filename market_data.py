
import pandas as pd
import requests
from io import StringIO

SYMBOL_MAP = {
"crudeoil":"usdtoil"
}

def get_data(asset):

    try:

        symbol = SYMBOL_MAP[asset]

        url = f"https://stooq.com/q/d/l/?s={symbol}&i=5"

        r = requests.get(url)

        if r.status_code != 200:
            return None

        df = pd.read_csv(StringIO(r.text))

        df.columns = ["date","open","high","low","close","volume"]

        return df.tail(200)

    except:
        return None
