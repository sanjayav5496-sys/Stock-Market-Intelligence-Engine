import pandas as pd
import numpy as np

# -------------------------------
# 📂 LOAD DATA
# -------------------------------
df = pd.read_csv("final_stock_intelligence_dataset.csv")

print("\n✅ DATA LOADED\n")

# -------------------------------
# 🔹 BASIC INFO
# -------------------------------
print("🔹 SHAPE:")
print(df.shape)

print("\n🔹 COLUMNS:")
print(df.columns)

print("\n🔹 INFO:")
df.info()

# -------------------------------
# 👀 HEAD & TAIL
# -------------------------------
print("\n🔹 HEAD:")
print(df.head())

print("\n🔹 TAIL:")
print(df.tail())

# -------------------------------
# 📊 DESCRIBE
# -------------------------------
print("\n🔹 DESCRIBE:")
print(df.describe())

# -------------------------------
# ❓ MISSING VALUES
# -------------------------------
print("\n🔹 MISSING VALUES:")
print(df.isnull().sum())

# -------------------------------
# 🔁 DUPLICATES
# -------------------------------
print("\n🔹 DUPLICATES:")
print(df.duplicated().sum())

# -------------------------------
# 📅 DATE ANALYSIS
# -------------------------------
df['Date'] = pd.to_datetime(df['Date'])

print("\n🔹 DATE RANGE:")
print("Start:", df['Date'].min())
print("End:", df['Date'].max())

# -------------------------------
# 📈 UNIQUE STOCKS
# -------------------------------
print("\n🔹 UNIQUE TICKERS:")
print(df['Ticker'].nunique())

# -------------------------------
# 📊 GROUP ANALYSIS
# -------------------------------
print("\n🔹 TOP 10 STOCKS (AVG CLOSE):")
print(df.groupby('Ticker')['Close'].mean().sort_values(ascending=False).head(10))

# -------------------------------
# 📈 RETURNS ANALYSIS
# -------------------------------
print("\n🔹 DAILY RETURN STATS:")
print(df['Daily_Return'].describe())

# -------------------------------
# 📊 CORRELATION
# -------------------------------
print("\n🔹 CORRELATION MATRIX:")
corr = df.select_dtypes(include=[np.number]).corr()
print(corr)

# -------------------------------
# 🔥 EXTREME VALUES
# -------------------------------
print("\n🔹 MAX RETURN:")
print(df.loc[df['Daily_Return'].idxmax()])

print("\n🔹 MIN RETURN:")
print(df.loc[df['Daily_Return'].idxmin()])

print("\n📊 FINAL DATASET INFO:")
print(df.info())

print("\n✅ EDA COMPLETED")