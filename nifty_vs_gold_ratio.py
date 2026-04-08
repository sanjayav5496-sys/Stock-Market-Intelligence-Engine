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
    # 2. Extract Close Prices
    # -----------------------------
    nifty_close = nifty["Close"].squeeze()
    gold_usd_close = gold_usd["Close"].squeeze()
    usd_inr_close = usd_inr["Close"].squeeze()

    # -----------------------------
    # 3. Convert Gold → INR/gram
    # -----------------------------
    gold_inr = (gold_usd_close * usd_inr_close) / 31.1035

    # -----------------------------
    # 4. Combine + Align Data
    # -----------------------------
    df = pd.concat(
        [
            nifty_close.rename("Nifty"),
            gold_inr.rename("Gold")
        ],
        axis=1
    ).dropna()

    # -----------------------------
    # 5. Ratio Calculation
    # -----------------------------
    df["Ratio"] = df["Nifty"] / df["Gold"]
    df["Ratio_Smooth"] = df["Ratio"].rolling(200).mean()

    # -----------------------------
    # 6. Proper Normalization (FIXED)
    # -----------------------------
    df_norm = (1 + df[["Nifty", "Gold"]].pct_change()).cumprod() * 100

    return df, df_norm


def get_decision(nifty_input, gold_input, df):
    # -----------------------------
    # Safety Check
    # -----------------------------
    if gold_input == 0:
        return None, None, "❌ Gold price cannot be zero"

    # -----------------------------
    # Ratio Logic
    # -----------------------------
    current_ratio = nifty_input / gold_input
    historical_avg = df["Ratio"].mean()

    # -----------------------------
    # Decision
    # -----------------------------
    if current_ratio > historical_avg:
        decision = "📉 Nifty is EXPENSIVE vs Gold → Prefer GOLD"
    elif current_ratio < historical_avg:
        decision = "📈 Nifty is CHEAP vs Gold → Prefer EQUITY"
    else:
        decision = "⚖️ Neutral Zone"

    return current_ratio, historical_avg, decision