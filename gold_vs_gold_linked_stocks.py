import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# 📊 FETCH DATA
# -------------------------------
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


# -------------------------------
# 📈 LINE CHARTS
# -------------------------------
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


# -------------------------------
# 📊 RETURNS CALCULATION
# -------------------------------
def get_gold_insights(data):

    data.index = pd.to_datetime(data.index)

    last_3y = data[data.index >= data.index.max() - pd.DateOffset(years=3)]

    returns = (last_3y.iloc[-1] / last_3y.iloc[0] - 1) * 100

    best = returns.idxmax()
    worst = returns.idxmin()

    return returns, best, worst


def plot_returns_bar(returns):

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(6, 3))

    names = returns.index
    values = returns.values

    # 🔵 Blue bars
    bars = ax.bar(names, values, color="#2E86C1", width=0.6)

    # ✅ Remove grid (MAIN FIX)
    ax.grid(False)

    # ✅ Remove top/right borders (clean look)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Optional: soften left/bottom
    ax.spines['left'].set_alpha(0.3)
    ax.spines['bottom'].set_alpha(0.3)

    # Value labels
    for i, v in enumerate(values):
        ax.text(i, v + (2 if v > 0 else -5), f"{v:.1f}%", 
                ha='center', fontsize=9)

    ax.set_title("3-Year Returns Comparison", fontsize=11)
    ax.set_ylabel("Returns (%)")

    ax.tick_params(axis='x', rotation=25)

    plt.tight_layout()
    return fig