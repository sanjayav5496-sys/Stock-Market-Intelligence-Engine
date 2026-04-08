import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

stocks = [
    "TCS.NS",
    "HDFCBANK.NS",
    "ITC.NS",
    "M&M.NS",
    "SUNPHARMA.NS",
    "TATASTEEL.NS",
    "RELIANCE.NS",
    "LT.NS",
    "DLF.NS",
    "ZEEL.NS",
    "BAJFINANCE.NS",
    "BHARTIARTL.NS"
]

def get_stock_correlation(start="2018-01-01"):
    data = yf.download(stocks, start=start)["Close"]

    data = data.dropna()

    returns = data.pct_change().dropna()
    corr = returns.corr()

    return corr


def plot_stock_correlation(corr):
    plt.figure(figsize=(9, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Cross-Sector Stock Correlation Heatmap")
    plt.tight_layout()
    return plt


def generate_stock_insights(corr):
    insights = []

    corr_unstack = corr.unstack()
    corr_unstack = corr_unstack[corr_unstack < 0.999]

    sorted_corr = corr_unstack.sort_values(ascending=False).drop_duplicates()

    # Top correlated
    for (s1, s2), val in sorted_corr.head(3).items():
        insights.append(
            f"🔗 {s1} & {s2} ({val:.2f}) → Similar movement (avoid overexposure)"
        )

    # Low correlated
    for (s1, s2), val in sorted_corr.tail(3).items():
        insights.append(
            f"🧊 {s1} & {s2} ({val:.2f}) → Good diversification pair"
        )

    return insights