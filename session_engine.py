
from datetime import datetime

def score():

    hour = datetime.utcnow().hour

    if 13 <= hour <= 17:
        return 20,"New York"

    if 7 <= hour <= 11:
        return 15,"London"

    if 0 <= hour <= 6:
        return 6,"Tokyo"

    return 3,"Sydney"
