
import config
from datetime import datetime

signals_today = []

def reset_day():

    global signals_today

    today = datetime.utcnow().date()

    signals_today = [s for s in signals_today if s["date"] == today]

def can_send_signal():

    reset_day()

    if len(signals_today) >= config.MAX_SIGNALS_PER_DAY:
        return False

    return True

def register_signal(signal):

    signals_today.append({
        "date": datetime.utcnow().date(),
        "score": signal["score"]
    })
