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

# -------------------------------
# 📊 CORRELATION
# -------------------------------
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
    plt.figure(figsize=(8, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Sector Correlation Heatmap")
    plt.tight_layout()
    return plt


def generate_insights(corr):
    insights = []

    corr_unstack = corr.unstack()
    corr_unstack = corr_unstack[corr_unstack < 0.999]

    top_pairs = corr_unstack.sort_values(ascending=False).drop_duplicates()

    for (s1, s2), val in top_pairs.head(3).items():
        insights.append(f"🔗 {s1} & {s2} → Strong correlation ({val:.2f})")

    for (s1, s2), val in top_pairs.tail(2).items():
        insights.append(f"🧊 {s1} & {s2} → Weak correlation ({val:.2f})")

    return insights


# -------------------------------
# 📈 VOLATILITY 
# -------------------------------
def get_sector_volatility(start="2000-01-01"):
    data = pd.DataFrame()

    for name, ticker in sectors.items():
        df = yf.download(ticker, start=start)["Close"]

        if not df.empty:
            data[name] = df

    data = data.dropna()

    returns = data.pct_change().dropna()

    volatility = returns.std() * (252 ** 0.5)
    volatility = volatility.sort_values(ascending=False)

    return volatility


def plot_sector_volatility(volatility):
    plt.figure(figsize=(8, 4))

    colors = []
    for v in volatility:
        if v > 0.28:
            colors.append("red")
        elif v > 0.22:
            colors.append("orange")
        else:
            colors.append("green")

    volatility.plot(kind="bar", color=colors)

    plt.title("Sector Volatility Comparison (Risk View)")
    plt.ylabel("Volatility")
    plt.xticks(rotation=45)
    plt.grid(axis="y")

    plt.tight_layout()
    return plt


def generate_volatility_insights(volatility):
    insights = []

    # Thresholds (based on your chart pattern)
    high = volatility[volatility > 0.27]
    medium = volatility[(volatility <= 0.27) & (volatility > 0.22)]
    low = volatility[volatility <= 0.20]

    # High Risk
    if not high.empty:
        sectors = ", ".join(high.index)
        insights.append(f"🔥 {sectors} → High volatility → Suitable for aggressive traders")

    # Medium Risk
    if not medium.empty:
        sectors = ", ".join(medium.index)
        insights.append(f"⚖️ {sectors} → Moderate volatility → Balanced risk")

    # Low Risk
    if not low.empty:
        sectors = ", ".join(low.index)
        insights.append(f"🛡️ {sectors} → Low volatility → Defensive / stable sectors")

    return insights

    return insights

# Portfolio
def get_portfolio_weights(corr, volatility):
    avg_corr = corr.mean()

    volatility = volatility.reindex(avg_corr.index)

    score = (1 - volatility) * (1 - avg_corr)

    weights = score / score.sum()

    return weights.sort_values(ascending=False)


def plot_portfolio(weights):
    plt.figure(figsize=(4, 4))

    wedges, texts, autotexts = plt.pie(
        weights,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.7,   # 👈 move % inside
        labeldistance=1.2  # 👈 move labels outside
    )

    plt.legend(wedges, weights.index, loc="center left", bbox_to_anchor=(1, 0.5))
    plt.title("Recommended Portfolio Allocation", fontsize=10)

    plt.tight_layout()
    return plt
   