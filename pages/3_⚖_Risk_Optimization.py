import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from risk_vs_return import (
    get_risk_return_data,
    plot_risk_return,
    generate_risk_insights
)

# -------------------------------
# 📊 COMBINED VERTICAL BAR PLOT
# -------------------------------
def plot_metric_combined(series, title, target=None):
    fig, ax = plt.subplots(figsize=(6,3))

    series = series.sort_values(ascending=False)

    # Color logic
    colors = []
    for v in series:
        if target is not None:
            colors.append("green" if v >= target else "red")
        else:
            colors.append("blue")

    series.plot(kind="bar", ax=ax, color=colors)

    # Target line
    if target is not None:
        ax.axhline(target, linestyle="--")

    ax.set_title(title)
    ax.set_ylabel("Value")
    ax.tick_params(axis='x', rotation=45)

    return fig


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def show_risk():
    st.title("⚖ Risk vs Return Analysis")

    df = get_risk_return_data()

    # -------------------------------
    # TOP SECTION
    # -------------------------------
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Risk vs Return")
        fig = plot_risk_return(df)
        st.pyplot(fig)

    with col2:
        st.subheader("📌 Key Insights")
        insights = generate_risk_insights(df)
        for ins in insights:
            st.write(ins)

    # -------------------------------
    # 🟢 ALPHA ANALYSIS
    # -------------------------------
    st.markdown("---")
    st.subheader("🟢 Alpha Analysis (Performance)")

    alpha_mean = df["Alpha"].mean()

    alpha_combined = pd.concat([
        df["Alpha"].sort_values(ascending=False).head(5),
        df["Alpha"].sort_values().head(5)
    ])

    alpha_combined = alpha_combined[~alpha_combined.index.duplicated()]

    st.pyplot(plot_metric_combined(alpha_combined, "Alpha Comparison", target=alpha_mean))

    st.info("Above line → High alpha (outperforming stocks)")

    # -------------------------------
    # 🔴 BETA ANALYSIS
    # -------------------------------
    st.markdown("---")
    st.subheader("🔴 Beta Analysis (Volatility)")

    beta_combined = pd.concat([
        df["Beta"].sort_values(ascending=False).head(5),
        df["Beta"].sort_values().head(5)
    ])

    beta_combined = beta_combined[~beta_combined.index.duplicated()]

    st.pyplot(plot_metric_combined(beta_combined, "Beta Comparison", target=1))

    st.info("Above 1 → Aggressive | Below 1 → Defensive")

    # -------------------------------
    # 🟡 SHARPE ANALYSIS
    # -------------------------------
    st.markdown("---")
    st.subheader("🟡 Sharpe Ratio Analysis (Efficiency)")

    sharpe_mean = df["Sharpe"].mean()

    sharpe_combined = pd.concat([
        df["Sharpe"].sort_values(ascending=False).head(5),
        df["Sharpe"].sort_values().head(5)
    ])

    sharpe_combined = sharpe_combined[~sharpe_combined.index.duplicated()]

    st.pyplot(plot_metric_combined(sharpe_combined, "Sharpe Comparison", target=sharpe_mean))

    st.info("Above line → Better risk-adjusted returns")


# -------------------------------
# RUN APP
# -------------------------------
show_risk()