import yfinance as yf
import pandas as pd


def get_nifty_gold_data():
    # -----------------------------
    # 1. Download Data
    # -----------------------------
    nifty = yf.download("^NSEI", period="max", progress=False)
    gold_usd = yf.download("GC=F", period="max", progress=False)
    usd_inr = yf.download("USDINR=X", period="max", progress=False)

    # -----------------------------
    # 2. Extract Close Prices (FIXED)
    # -----------------------------
    def get_close(df, name):
        series = df["Close"]
        if isinstance(series, pd.DataFrame):
            series = series.iloc[:, 0]
        return series.rename(name)

    nifty_close = get_close(nifty, "Nifty")
    gold_usd_close = get_close(gold_usd, "Gold_USD")
    usd_inr_close = get_close(usd_inr, "USDINR")

    # -----------------------------
    # 3. Combine FIRST (important)
    # -----------------------------
    df = pd.concat([nifty_close, gold_usd_close, usd_inr_close], axis=1).dropna()

    # -----------------------------
    # 4. Convert Gold → INR/gram
    # -----------------------------
    df["Gold"] = (df["Gold_USD"] * df["USDINR"]) / 31.1035

    # -----------------------------
    # 5. Ratio Calculation
    # -----------------------------
    df["Ratio"] = df["Nifty"] / df["Gold"]

    # 🚨 Sanity filter (VERY IMPORTANT)
    df = df[(df["Ratio"] > 0.5) & (df["Ratio"] < 10)]

    # -----------------------------
    # 6. Smooth Ratio
    # -----------------------------
    df["Ratio_Smooth"] = df["Ratio"].rolling(200, min_periods=50).mean()

    # -----------------------------
    # 7. Normalization (SAFE)
    # -----------------------------
    df_norm = df[["Nifty", "Gold"]].pct_change().add(1).cumprod() * 100

    return df, df_norm


def get_decision(nifty_input, gold_input, df):
    if gold_input == 0:
        return None, None, "❌ Gold price cannot be zero"

    current_ratio = nifty_input / gold_input

    # Use median instead of mean (more stable)
    historical_avg = df["Ratio"].median()

    # -----------------------------
    # Decision Logic
    # -----------------------------
    if current_ratio > historical_avg * 1.1:
        decision = "📉 Nifty is EXPENSIVE than Gold → Prefer GOLD"
    elif current_ratio < historical_avg * 0.9:
        decision = "📈 Nifty is CHEAPER than Gold → Prefer EQUITY"
    else:
        decision = "⚖️ Neutral Zone"

    return current_ratio, historical_avg, decision