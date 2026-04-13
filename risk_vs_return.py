import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stocks = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
    "KOTAKBANK.NS","SBIN.NS","AXISBANK.NS","LT.NS","ITC.NS",
    "HINDUNILVR.NS","BHARTIARTL.NS","ASIANPAINT.NS","MARUTI.NS",
    "SUNPHARMA.NS","ULTRACEMCO.NS","TITAN.NS","NESTLEIND.NS",
    "POWERGRID.NS","NTPC.NS","ONGC.NS","BAJFINANCE.NS"
]

nifty = "^NSEI"


# ================================
# 📊 DATA FUNCTION
# ================================
def get_risk_return_data(start="2018-01-01"):
    raw_data = yf.download(stocks + [nifty], start=start)

    data = raw_data["Close"].dropna()
    returns = data.pct_change().dropna()

    mean_returns = returns.mean() * 252
    risk = returns.std() * np.sqrt(252)

    market_returns = returns[nifty]

    beta = {}
    for stock in stocks:
        cov = np.cov(returns[stock], market_returns)[0][1]
        beta[stock] = cov / market_returns.var()

    beta = pd.Series(beta)

    rf = 0.06
    market_return = mean_returns[nifty]

    alpha = {}
    for stock in stocks:
        alpha[stock] = mean_returns[stock] - (
            rf + beta[stock] * (market_return - rf)
        )

    alpha = pd.Series(alpha)

    sharpe = (mean_returns[stocks] - rf) / risk[stocks]

    df = pd.DataFrame({
        "Return": mean_returns[stocks],
        "Risk": risk[stocks],
        "Alpha": alpha,
        "Beta": beta,
        "Sharpe": sharpe
    })

    df = df.sort_values(by="Sharpe", ascending=False)

    return df


# ================================
# 📈 RISK vs RETURN
# ================================
def plot_risk_return(df):

    fig, ax = plt.subplots(figsize=(6, 4))  # 👈 controlled size

    for stock in df.index:
        ax.scatter(df.loc[stock, "Risk"], df.loc[stock, "Return"])
        ax.text(
            df.loc[stock, "Risk"],
            df.loc[stock, "Return"],
            stock.replace(".NS", ""),
            fontsize=6
        )

    ax.set_xlabel("Risk")
    ax.set_ylabel("Return")
    ax.set_title("Risk vs Return")

    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    return fig


# ================================
# 📌 INSIGHTS
# ================================
def generate_risk_insights(df):
    insights = []

    for stock in df.head(3).index:
        insights.append(f"🏆 {stock} → High Sharpe (efficient stock)")

    for stock in df.sort_values(by="Beta", ascending=False).head(2).index:
        insights.append(f"⚡ {stock} → High beta (volatile)")

    for stock in df.sort_values(by="Beta").head(2).index:
        insights.append(f"🛡 {stock} → Defensive stock")

    return insights


# ================================
# 📊 GENERIC CLEAN BAR FUNCTION
# ================================
def plot_metric(series, title, target=None):

    series = series.sort_values()

    fig, ax = plt.subplots(figsize=(5, 3))  # 👈 perfect size

    # Color logic
    if target is not None:
        colors = ["green" if v >= target else "red" for v in series]
    else:
        colors = "#2E86C1"

    series.plot(kind="bar", ax=ax, color=colors, width=0.6)

    # Target line
    if target is not None:
        ax.axhline(target, linestyle="--")

    # Clean UI
    ax.set_title(title, fontsize=10)
    ax.set_ylabel("Value", fontsize=9)

    ax.tick_params(axis='x', rotation=30, labelsize=8)

    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    return fig


# ================================
# 📊 ALPHA / BETA / SHARPE WRAPPERS
# ================================
def plot_alpha(alpha_series):
    return plot_metric(
        alpha_series,
        "Alpha Comparison",
        target=alpha_series.mean()
    )


def plot_beta(beta_series):
    return plot_metric(
        beta_series,
        "Beta Comparison",
        target=1
    )


def plot_sharpe(sharpe_series):
    return plot_metric(
        sharpe_series,
        "Sharpe Ratio",
        target=sharpe_series.mean()
    )