import streamlit as st
import matplotlib.pyplot as plt
from nifty_vs_gold_ratio import get_nifty_gold_data, get_decision

# ✅ CACHE FIX (CRITICAL)
@st.cache_data
def load_data():
    return get_nifty_gold_data()


def show_nifty_gold():
    st.title("⚖ Nifty vs Gold Analysis")

    df, df_norm = load_data()

    # -----------------------------
    # Charts
    # -----------------------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Top chart
    ax1.plot(df_norm.index, df_norm["Nifty"], label="Nifty")
    ax1.plot(df_norm.index, df_norm["Gold"], label="Gold (₹/g)")
    ax1.set_title("Nifty vs Gold (Normalized)")
    ax1.legend()
    ax1.grid()

    # Bottom chart
    ax2.plot(df.index, df["Ratio"], color="gray", alpha=0.3, label="Raw")
    ax2.plot(df.index, df["Ratio_Smooth"], color="blue", label="200 DMA")
    ax2.axhline(df["Ratio"].median(), linestyle="--", color="black", label="Median")

    ax2.set_title("Nifty / Gold Ratio")
    ax2.legend()
    ax2.grid()

    st.pyplot(fig)

    # -----------------------------
    # RESET BUTTON (IMPORTANT)
    # -----------------------------
    if st.button("🔄 Reset Data"):
        st.cache_data.clear()
        st.rerun()

    # -----------------------------
    # User Input
    # -----------------------------
    st.markdown("---")
    st.subheader("Nifty to Gold Ratio Calculator")

    col1, col2 = st.columns(2)

    with col1:
        nifty_input = st.number_input("Nifty Value", value=23000.0)

    with col2:
        gold_input = st.number_input("Gold (₹/gram)", value=7000.0)

    # -----------------------------
    # Decision
    # -----------------------------
    if st.button("Analyze Market"):

        current_ratio, historical_avg, decision = get_decision(
            nifty_input, gold_input, df
        )

        st.markdown("---")
        st.subheader("📊 Result")

        st.metric("Current Ratio", f"{current_ratio:.2f}")
        st.metric("Historical Avg", f"{historical_avg:.2f}")

        if "EXPENSIVE" in decision:
            st.error(decision)
        elif "CHEAP" in decision:
            st.success(decision)
        else:
            st.info(decision)


show_nifty_gold()