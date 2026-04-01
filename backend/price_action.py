# Trading logic
def analyze_market(data):
    close = data["Close"].iloc[-1]
    high = data["High"].max()
    low = data["Low"].min()

    # Liquidity sweep logic (simplified)
    if close > high * 0.99:  # breakout above resistance
        return {"action": "BUY", "stop_loss": low}
    elif close < low * 1.01:  # breakdown below support
        return {"action": "SELL", "stop_loss": high}
    else:
        return {"action": "WAIT", "stop_loss": None}
