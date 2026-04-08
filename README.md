# 📊 Stock Market Intelligence Engine

An advanced **data-driven stock market analytics platform** built using Streamlit.
This project uncovers hidden relationships between **sectors, stocks, commodities, and macro indicators** to support smarter investment decisions.

---

## 🚀 Live App
https://stock-market-intelligence-engine-xygzbutvucq6yjeuzg3vu3.streamlit.app/

---

## 🧠 Key Features

### 🔗 Sector Correlation

* Analyze how different market sectors move together
* Identify diversification opportunities
* Detect macro-driven sector clusters

---

### 📈 Stock Correlation

* Understand relationships between major stocks
* Avoid overexposure to highly correlated assets
* Discover diversification pairs

---

### ⚖️ Risk vs Return Analysis

* Compare stocks based on:

  * Risk (volatility)
  * Return
  * Alpha
  * Beta
  * Sharpe Ratio
* Identify:

  * Top Alpha stocks
  * High Beta (volatile) stocks
  * Low Beta (defensive) stocks
  * High Sharpe (efficient) stocks

---

### 🪙 Nifty vs Gold Analysis

* Compares equity vs commodity performance
* Uses **Nifty/Gold Ratio** as a macro indicator
* Helps identify:

  * When equity is expensive
  * When gold is preferable

---

### ⛽ Commodity Analysis

#### 🪙 Gold vs Gold-linked Stocks

* Tracks gold alongside:

  * Muthoot Finance
  * Manappuram
  * Titan
  * Kalyan Jewellers

#### 🛢 Crude Oil vs Linked Stocks

* Analyzes crude oil impact on:

  * ONGC (upstream beneficiary)
  * IOCL (refining margins)
  * Asian Paints (input cost impact)
  * Apollo Tyres (raw material dependency)

---

## 📊 Insights Engine

The app doesn’t just show charts — it explains them.

Examples:

* High correlation → avoid holding both stocks
* Low correlation → diversification opportunity
* Commodity rise → sector-specific impact
* Nifty vs Gold → macro allocation signal

---

## 🏗️ Project Structure

```
nifty_intelligence_engine/
│
├── Home.py
├── requirements.txt
│
├── pages/
│   ├── 1_Sector.py
│   ├── 2_Stock.py
│   ├── 3_Nifty_vs_Gold.py
│   ├── 4_Risk_vs_Return.py
│   ├── 5_Commodity.py
│
├── sector_correlation.py
├── stock_correlation.py
├── risk_return.py
├── nifty_vs_gold.py
├── gold_vs_gold_linked_stocks.py
├── crude_vs_linked_stocks.py
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **yFinance**

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/sanjayav5496-sys/Stock-Market-Intelligence-Engine.git
cd Stock-Market-Intelligence-Engine
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the app

```
streamlit run Home.py
```

---

## 🚀 Deployment

This app is deployed using **Streamlit Community Cloud**.

To deploy:

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Select repository
4. Set main file → `Home.py`

---

## 📌 Key Learnings

* Multi-layer financial data analysis
* Correlation-based portfolio design
* Commodity-stock relationships
* Risk-adjusted performance metrics
* Building modular Streamlit applications
* Deploying real-world data apps

---

## 🔮 Future Improvements

* Live signals based on macro indicators
* Portfolio optimization engine
* Interactive filters for stocks/sectors
* Real-time alerts
* Advanced visualizations (Plotly)

---

## 👤 Author

**Sanjay A V**

* Passionate about stock markets & data analytics
* Building intelligent financial tools

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
