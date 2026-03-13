import indicators
import score_engine
import session_engine
import risk_engine
import config

def analyze_market(data, asset):

    df5, df1 = data

    # ======================
    # INDICATORI 5M
    # ======================

    df5["ema20"] = indicators.ema(df5["close"],20)
    df5["ema50"] = indicators.ema(df5["close"],50)
    df5["ema200"] = indicators.ema(df5["close"],200)

    df5["rsi"] = indicators.rsi(df5["close"])
    df5["atr"] = indicators.atr(df5)

    last = df5.iloc[-1]

    # ======================
    # TREND 1H
    # ======================

    df1["ema50"] = indicators.ema(df1["close"],50)
    df1["ema200"] = indicators.ema(df1["close"],200)

    trend_htf = df1.iloc[-1]["ema50"] > df1.iloc[-1]["ema200"]

    # ======================
    # TREND LOCALE
    # ======================

    trend = last["ema50"] > last["ema200"] and trend_htf

    # ======================
    # MOMENTUM
    # ======================

    momentum = last["rsi"] > 60

    # ======================
    # VOLUME SPIKE (meno rigido)
    # ======================

    vol_avg = df5["volume"].rolling(20).mean().iloc[-1]

    volume = last["volume"] > vol_avg * 1.2

    # ======================
    # VOLATILITA
    # ======================

    atr_avg = df5["atr"].rolling(20).mean().iloc[-1]

    volatility = last["atr"] > atr_avg

    # ======================
    # LIQUIDITY SWEEP
    # ======================

    prev_low = df5["low"].rolling(8).min().iloc[-2]

    liquidity = last["low"] < prev_low and last["close"] > prev_low

    # ======================
    # PULLBACK
    # ======================

    pullback = last["close"] <= last["ema20"]

    # ======================
    # SESSION SCORE
    # ======================

    session_pts, session_name = session_engine.score()

    # ======================
    # SCORE
    # ======================

    score = score_engine.calculate({
        "trend":trend,
        "liquidity":liquidity,
        "volume":volume,
        "volatility":volatility,
        "momentum":momentum,
        "pullback":pullback,
        "session":session_pts
    })

    print("Score:", score)

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
