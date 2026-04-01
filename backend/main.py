# FastAPI backend
from fastapi import FastAPI
import yfinance as yf
from price_action import analyze_market

app = FastAPI()

@app.get("/signal/{pair}")
def get_signal(pair: str):
    data = yf.download(pair, period="1d", interval="15m")
    signal = analyze_market(data)
    return {"pair": pair, "signal": signal}
