import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sector indices
sectors = {
    "IT": "^CNXIT",
    "Bank": "^NSEBANK",
    "FMCG": "^CNXFMCG",
    "Auto": "^CNXAUTO",
    "Pharma": "^CNXPHARMA",
    "Metal": "^CNXMETAL",
    "Energy": "^CNXENERGY",
    "Infra": "^CNXINFRA",
    "Realty": "^CNXREALTY",
    "Media": "^CNXMEDIA"
}

def get_sector_correlation(start="2000-01-01"):
    data = pd.DataFrame()

    for name, ticker in sectors.items():
        df = yf.download(ticker, start=start)["Close"]

        if not df.empty:
            data[name] = df

    data = data.dropna()
    returns = data.pct_change().dropna()
    corr = returns.corr()

    return corr


def plot_sector_correlation(corr):
    plt.figure(figsize=(8, 5))  # smaller chart
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Sector Correlation Heatmap")
    plt.tight_layout()
    return plt


def generate_insights(corr):
    insights = []

    corr_unstack = corr.unstack()
    corr_unstack = corr_unstack[corr_unstack < 0.999]

    top_pairs = corr_unstack.sort_values(ascending=False).drop_duplicates()

    # Top correlations
    for (s1, s2), val in top_pairs.head(3).items():
        insights.append(f"🔗 {s1} & {s2} → Strong correlation ({val:.2f})")

    # Lowest correlations
    for (s1, s2), val in top_pairs.tail(2).items():
        insights.append(f"🧊 {s1} & {s2} → Weak correlation ({val:.2f})")

    return insights