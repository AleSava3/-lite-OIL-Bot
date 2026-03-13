
import indicators
import score_engine
import session_engine
import risk_engine
import config

def analyze_market(df,asset):

    df["ema20"] = indicators.ema(df["close"],20)
    df["ema50"] = indicators.ema(df["close"],50)
    df["ema200"] = indicators.ema(df["close"],200)

    df["rsi"] = indicators.rsi(df["close"])
    df["atr"] = indicators.atr(df)

    last = df.iloc[-1]

    trend = last["ema50"] > last["ema200"]

    momentum = last["rsi"] > 60

    vol_avg = df["volume"].rolling(20).mean().iloc[-1]

    volume = last["volume"] > vol_avg*1.5

    atr_avg = df["atr"].rolling(20).mean().iloc[-1]

    volatility = last["atr"] > atr_avg

    prev_low = df["low"].rolling(8).min().iloc[-2]

    liquidity = last["low"] < prev_low and last["close"] > prev_low

    pullback = last["close"] <= last["ema20"]

    session_pts,session_name = session_engine.score()

    score = score_engine.calculate({
        "trend":trend,
        "liquidity":liquidity,
        "volume":volume,
        "volatility":volatility,
        "momentum":momentum,
        "pullback":pullback,
        "session":session_pts
    })

    if score < config.MIN_SCORE:
        return None

    price = last["close"]
    atr = last["atr"]

    sl,tp,rr = risk_engine.levels(asset,price,atr)

    invest = score >= config.INVEST_SCORE

    return {
        "asset":asset,
        "direction":"BUY",
        "entry":price,
        "sl":sl,
        "tp":tp,
        "rr":rr,
        "score":score,
        "session":session_name,
        "invest":invest
    }
