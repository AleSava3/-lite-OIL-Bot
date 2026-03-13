
def calculate(data):

    score = 0

    if data["trend"]:
        score += 20

    if data["liquidity"]:
        score += 15

    if data["volume"]:
        score += 15

    if data["volatility"]:
        score += 10

    if data["momentum"]:
        score += 10

    if data["pullback"]:
        score += 5

    score += data["session"]

    return score
