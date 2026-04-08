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


def plot_risk_return(df):
    plt.figure(figsize=(8, 5))

    for stock in df.index:
        plt.scatter(df.loc[stock, "Risk"], df.loc[stock, "Return"])
        plt.text(df.loc[stock, "Risk"], df.loc[stock, "Return"],
                 stock.replace(".NS", ""), fontsize=7)

    plt.xlabel("Risk")
    plt.ylabel("Return")
    plt.title("Risk vs Return")
    plt.grid()

    return plt


def generate_risk_insights(df):
    insights = []

    # Top Sharpe
    for stock in df.head(3).index:
        insights.append(f"🏆 {stock} → High Sharpe (efficient stock)")

    # High Beta
    for stock in df.sort_values(by="Beta", ascending=False).head(2).index:
        insights.append(f"⚡ {stock} → High beta (volatile)")

    # Low Beta
    for stock in df.sort_values(by="Beta").head(2).index:
        insights.append(f"🛡 {stock} → Defensive stock")

    return insights