import streamlit as st
from risk_vs_return import (
    get_risk_return_data,
    plot_risk_return,
    generate_risk_insights
)

def show_risk():
    st.title("⚖ Risk vs Return Analysis")

    # Get data
    df = get_risk_return_data()

    # Top layout
    col1, col2 = st.columns([2, 1])

    # LEFT → Chart
    with col1:
        st.subheader("📊 Risk vs Return")
        fig = plot_risk_return(df)
        st.pyplot(fig)

    # RIGHT → Insights
    with col2:
        st.subheader("📌 Key Insights")

        insights = generate_risk_insights(df)
        for ins in insights:
            st.write(ins)

    # Bottom section
    st.markdown("---")
    st.subheader("📊 Stock Rankings")

    col3, col4 = st.columns(2)

    with col3:
        st.write("### 🟢 Top 5 Alpha Stocks")
        alpha_top = df.sort_values(by="Alpha", ascending=False).head(5)
        for stock in alpha_top.index:
            st.write(f"🚀 {stock} → Alpha: {alpha_top.loc[stock, 'Alpha']:.2f}")

        st.write("### 🔴 High Beta Stocks")
        high_beta = df.sort_values(by="Beta", ascending=False).head(5)
        for stock in high_beta.index:
            st.write(f"⚡ {stock} → Beta: {high_beta.loc[stock, 'Beta']:.2f}")

    with col4:
        st.write("### 🔵 Low Beta Stocks")
        low_beta = df.sort_values(by="Beta").head(5)
        for stock in low_beta.index:
            st.write(f"🛡 {stock} → Beta: {low_beta.loc[stock, 'Beta']:.2f}")

        st.write("### 🟡 High Sharpe Ratio")
        sharpe_top = df.sort_values(by="Sharpe", ascending=False).head(5)
        for stock in sharpe_top.index:
            st.write(f"🏆 {stock} → Sharpe: {sharpe_top.loc[stock, 'Sharpe']:.2f}")

# IMPORTANT
show_risk()