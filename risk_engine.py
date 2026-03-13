
import config

def levels(asset,price,atr):

    sl = price - atr*config.ATR_SL_OIL
    tp = price + atr*config.ATR_TP_OIL

    rr = abs(tp-price)/abs(price-sl)

    return sl,tp,rr
