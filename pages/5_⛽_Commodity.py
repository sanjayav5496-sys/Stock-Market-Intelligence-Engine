import streamlit as st

# GOLD IMPORTS (also contains plot_returns_bar)
from gold_vs_gold_linked_stocks import (
    get_gold_data,
    plot_gold,
    get_gold_insights,
    plot_returns_bar   # ✅ use this for both
)

# CRUDE IMPORTS
from crude_vs_linked_stocks import (
    get_crude_data,
    plot_crude,
    get_crude_insights
)


def show_commodity():

    st.title("⛽ Commodity Analysis")

    # RADIO BUTTON
    option = st.radio(
        "Choose Commodity",
        ["🪙 Gold", "🛢 Crude Oil"],
        horizontal=True
    )

    st.markdown("---")

    # =========================
    # 🪙 GOLD SECTION
    # =========================
    if option == "🪙 Gold":

        data, norm = get_gold_data()

        col1, col2 = st.columns([2, 1])

        # LEFT → CHARTS
        with col1:
            fig = plot_gold(norm)
            st.pyplot(fig)

            returns, best, worst = get_gold_insights(data)

            st.subheader("📊 3-Year Returns (Comparison)")
            fig2 = plot_returns_bar(returns)   # ✅ BLUE BAR
            st.pyplot(fig2)

        # RIGHT → INSIGHTS
        with col2:
            returns, best, worst = get_gold_insights(data)

            st.subheader("📊 Returns Summary")
            for col in returns.index:
                st.write(f"{col}: {returns[col]:.2f}%")

            st.markdown("---")
            st.subheader("📌 Insights")

            st.write(f"🚀 Best performer: {best}")
            st.write(f"⚠️ Weak performer: {worst}")

    # =========================
    # 🛢 CRUDE SECTION
    # =========================
    elif option == "🛢 Crude Oil":

        data, norm = get_crude_data()

        col1, col2 = st.columns([2, 1])

        # LEFT → CHARTS
        with col1:
            fig = plot_crude(norm)
            st.pyplot(fig)

            returns, best, worst, logic = get_crude_insights(data)

            st.subheader("📊 3-Year Returns (Comparison)")
            fig2 = plot_returns_bar(returns)   # ✅ SAME FUNCTION
            st.pyplot(fig2)

        # RIGHT → INSIGHTS
        with col2:
            returns, best, worst, logic = get_crude_insights(data)

            st.subheader("📊 Returns Summary")
            for col in returns.index:
                st.write(f"{col}: {returns[col]:.2f}%")

            st.markdown("---")
            st.subheader("📌 Insights")

            st.write(f"🚀 Best performer: {best}")
            st.write(f"⚠️ Weak performer: {worst}")

            st.markdown("### 🧠 Market Logic")
            st.write(logic)


# RUN APP
show_commodity()