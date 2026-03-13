import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

MAX_SIGNALS_PER_DAY = 20

# score minimo più flessibile
MIN_SCORE = 80

# segnali top
INVEST_SCORE = 92

# risk management crude oil
ATR_SL_OIL = 1.5
ATR_TP_OIL = 3.2

STATS_FILE = "trade_stats.csv"
