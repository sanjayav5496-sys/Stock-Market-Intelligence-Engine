import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_gold_data():

    tickers = {
        "Gold": "GC=F",
        "Muthoot": "MUTHOOTFIN.NS",
        "Manappuram": "MANAPPURAM.NS",
        "Titan": "TITAN.NS",
        "Kalyan": "KALYANKJIL.NS"
    }

    raw = yf.download(list(tickers.values()), start="2015-01-01", progress=False)

    data = raw["Adj Close"] if "Adj Close" in raw else raw["Close"]

    data = data.dropna(axis=1, how='all')

    reverse_map = {v: k for k, v in tickers.items()}
    data.columns = [reverse_map.get(col, col) for col in data.columns]

    data = data.dropna()

    norm = data / data.iloc[0] * 100

    return data, norm


def plot_gold(norm):

    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(norm.index, norm["Gold"])
    axes[0].set_title("Gold")

    for col in ["Muthoot", "Manappuram"]:
        if col in norm:
            axes[1].plot(norm.index, norm[col], label=col)
    axes[1].legend()
    axes[1].set_title("Gold Finance")

    for col in ["Titan", "Kalyan"]:
        if col in norm:
            axes[2].plot(norm.index, norm[col], label=col)
    axes[2].legend()
    axes[2].set_title("Jewellery")

    for ax in axes:
        ax.grid()

    plt.tight_layout()
    return fig


def get_gold_insights(data):

    data.index = pd.to_datetime(data.index)  
    last_3y = data[data.index >= data.index.max() - pd.DateOffset(years=3)]
    returns = (last_3y.iloc[-1] / last_3y.iloc[0] - 1) * 100

    best = returns.idxmax()
    worst = returns.idxmin()

    return returns, best, worst