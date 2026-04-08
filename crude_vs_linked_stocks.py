import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_crude_data():

    tickers = {
        "Crude Oil": "CL=F",
        "Asian Paints": "ASIANPAINT.NS",
        "Apollo Tyres": "APOLLOTYRE.NS",
        "IOCL": "IOC.NS",
        "ONGC": "ONGC.NS"
    }

    raw = yf.download(list(tickers.values()), start="2015-01-01")

    if isinstance(raw.columns, pd.MultiIndex):
        data = raw["Adj Close"] if "Adj Close" in raw.columns.levels[0] else raw["Close"]
    else:
        data = raw

    data.columns = tickers.keys()

    data = data.ffill().dropna()

    norm = data / data.iloc[0] * 100

    return data, norm


def plot_crude(norm):

    fig, axes = plt.subplots(5, 1, figsize=(10, 10), sharex=True)

    for i, col in enumerate(norm.columns):
        axes[i].plot(norm.index, norm[col])
        axes[i].set_title(col)
        axes[i].grid()

    plt.tight_layout()
    return fig


def get_crude_insights(data):

    last_3y = data.last("3Y")
    returns = (last_3y.iloc[-1] / last_3y.iloc[0] - 1) * 100

    best = returns.idxmax()
    worst = returns.idxmin()

    logic = """
• Rising crude → negative for paint & tyres (input cost increases)  
• Rising crude → positive for upstream (ONGC)  
• Oil marketing companies (IOCL) depend on margins  
"""

    return returns, best, worst, logic