
import pandas as pd
import os
import config
from datetime import datetime

def record_signal(signal):

    row = {
        "time": datetime.utcnow(),
        "asset": signal["asset"],
        "direction": signal["direction"],
        "entry": signal["entry"],
        "sl": signal["sl"],
        "tp": signal["tp"],
        "score": signal["score"]
    }

    if not os.path.exists(config.STATS_FILE):

        df = pd.DataFrame([row])
        df.to_csv(config.STATS_FILE,index=False)

    else:

        df = pd.read_csv(config.STATS_FILE)
        df = pd.concat([df,pd.DataFrame([row])])
        df.to_csv(config.STATS_FILE,index=False)
