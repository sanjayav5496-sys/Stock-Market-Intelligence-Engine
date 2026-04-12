import yfinance as yf
import pandas as pd

# -------------------------------
# ✅ NIFTY 50 STOCKS (EXCEPT TATA MOTORS)
# -------------------------------
nifty50 = [
    "RELIANCE.NS","HDFCBANK.NS","INFY.NS","ICICIBANK.NS","TCS.NS",
    "HINDUNILVR.NS","KOTAKBANK.NS","LT.NS","SBIN.NS","ITC.NS",
    "AXISBANK.NS","BAJFINANCE.NS","BHARTIARTL.NS","ASIANPAINT.NS",
    "MARUTI.NS","SUNPHARMA.NS","ULTRACEMCO.NS","NESTLEIND.NS",
    "WIPRO.NS","NTPC.NS","POWERGRID.NS","TITAN.NS","ADANIENT.NS",
    "ADANIPORTS.NS","JSWSTEEL.NS","HCLTECH.NS","TECHM.NS",
    "DRREDDY.NS","CIPLA.NS","EICHERMOT.NS","GRASIM.NS",
    "HEROMOTOCO.NS","BAJAJFINSV.NS","BAJAJ-AUTO.NS","INDUSINDBK.NS",
    "COALINDIA.NS","BPCL.NS","DIVISLAB.NS","BRITANNIA.NS",
    "APOLLOHOSP.NS","SBILIFE.NS","HDFCLIFE.NS","TATACONSUM.NS",
    "UPL.NS","ONGC.NS","IOC.NS"
]

# -------------------------------
# ✅ EXTRA STOCKS
# -------------------------------
extra_stocks = [
    "MUTHOOTFIN.NS","MANAPPURAM.NS","TITAN.NS","KALYANKJIL.NS",
    "ASIANPAINT.NS","APOLLOTYRE.NS","IOC.NS","ONGC.NS"
]

# -------------------------------
# 🔄 COMBINE STOCKS
# -------------------------------
stock_tickers = list(set(nifty50 + extra_stocks))

# -------------------------------
# 📅 DOWNLOAD STOCK DATA
# -------------------------------
stock_data = []

for ticker in stock_tickers:
    try:
        df = yf.download(
            ticker,
            start="2022-01-01",
            end="2024-12-31",
            auto_adjust=True
        )

        if df.empty:
            print(f"⚠️ No data for {ticker}")
            continue

        # Flatten MultiIndex if exists
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.reset_index(inplace=True)
        df = df[['Date', 'Open', 'High', 'Low', 'Close']]
        df['Ticker'] = ticker

        stock_data.append(df)

        print(f"✅ Loaded: {ticker}")

    except Exception as e:
        print(f"❌ Error with {ticker}: {e}")

# -------------------------------
# ❗ SAFETY CHECK
# -------------------------------
if not stock_data:
    raise ValueError("❌ No stock data downloaded. Check internet or yfinance.")

# -------------------------------
# COMBINE ALL STOCKS
# -------------------------------
final_df = pd.concat(stock_data)
final_df.sort_values(by=['Date', 'Ticker'], inplace=True)
final_df.reset_index(drop=True, inplace=True)

# -------------------------------
# 📊 CLEAN YFINANCE FUNCTION
# -------------------------------
def clean_yf(df, col_name):
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df[['Close']].rename(columns={'Close': col_name})
    df = df.reset_index()

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    return df

# -------------------------------
# 📊 FETCH MACRO DATA
# -------------------------------
nifty = clean_yf(
    yf.download("^NSEI", start="2022-01-01", end="2024-12-31"),
    "Nifty_Value"
)

gold = clean_yf(
    yf.download("GC=F", start="2022-01-01", end="2024-12-31"),
    "Gold_Price"
)

crude = clean_yf(
    yf.download("CL=F", start="2022-01-01", end="2024-12-31"),
    "Crude_Oil"
)

# -------------------------------
# 🔗 MERGE MACRO DATA (SAFE)
# -------------------------------
macro = nifty.merge(gold, on='Date', how='outer') \
             .merge(crude, on='Date', how='outer')

# -------------------------------
# ⚠️ ENSURE DATE FORMAT
# -------------------------------
final_df['Date'] = pd.to_datetime(final_df['Date'], errors='coerce')
macro['Date'] = pd.to_datetime(macro['Date'], errors='coerce')

# -------------------------------
# 🔗 MERGE STOCK + MACRO (FINAL FIX)
# -------------------------------
final_df = final_df.merge(macro, on='Date', how='left')

# -------------------------------
# 📈 DAILY RETURNS
# -------------------------------
final_df = final_df.sort_values(by=['Ticker', 'Date'])
final_df['Daily_Return'] = final_df.groupby('Ticker')['Close'].pct_change() * 100
final_df['Daily_Return'] = final_df['Daily_Return'].fillna(0)

# -------------------------------
# 🧹 CLEAN DATA
# -------------------------------
final_df.dropna(subset=['Close'], inplace=True)

# Fill macro missing values (important)
final_df[['Nifty_Value','Gold_Price','Crude_Oil']] = \
    final_df[['Nifty_Value','Gold_Price','Crude_Oil']].ffill()

# -------------------------------
# ✅ FINAL COLUMN ORDER
# -------------------------------
final_df = final_df[
    ['Date','Open','High','Low','Close','Ticker',
     'Nifty_Value','Gold_Price','Crude_Oil','Daily_Return']
]

# -------------------------------
# 💾 SAVE CSV
# -------------------------------
output_path = r"C:\Users\sanja\OneDrive\Documents\nifty_intelligence_engine\final_stock_intelligence_dataset.csv"
final_df.to_csv(output_path, index=False)

# -------------------------------
# ✅ CONFIRMATION
# -------------------------------
print("\n✅ DATASET CREATED SUCCESSFULLY")
print("📁 Saved at:", output_path)
print("📊 Shape:", final_df.shape)
print("📈 Unique Stocks:", final_df['Ticker'].nunique())