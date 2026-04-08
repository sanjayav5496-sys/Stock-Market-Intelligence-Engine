import streamlit as st

# GOLD IMPORTS (your existing file)
from gold_vs_gold_linked_stocks import (
    get_gold_data,
    plot_gold,
    get_gold_insights
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

        with col1:
            fig = plot_gold(norm)
            st.pyplot(fig)

        with col2:
            returns, best, worst = get_gold_insights(data)

            st.subheader("📊 3-Year Returns")
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

        with col1:
            fig = plot_crude(norm)
            st.pyplot(fig)

        with col2:
            # ✅ FIXED LINE (no more error)
            returns, best, worst, logic = get_crude_insights(data)

            st.subheader("📊 3-Year Returns")
            for col in returns.index:
                st.write(f"{col}: {returns[col]:.2f}%")

            st.markdown("---")
            st.subheader("📌 Insights")

            st.write(f"🚀 Best performer: {best}")
            st.write(f"⚠️ Weak performer: {worst}")

            st.markdown("### 🧠 Market Logic")
            st.write(logic)



show_commodity()