
import requests
import config

def send_signal(s):

    if s["invest"]:
        tag = "🔥 INVEST SETUP"
    else:
        tag = "Signal"

    msg=f'''
🚨 ELITE BOT CRUDE OIL

{tag}

Asset: {s['asset']}
Direction: {s['direction']}

Entry: {round(s['entry'],4)}
SL: {round(s['sl'],4)}
TP: {round(s['tp'],4)}

RR: {round(s['rr'],2)}
Score: {s['score']}
Session: {s['session']}
'''

    url=f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"

    requests.post(url,json={
        "chat_id":config.CHAT_ID,
        "text":msg
    })
