import streamlit as st
from sector_correlation import (
    get_sector_correlation,
    plot_sector_correlation,
    generate_insights,
    get_sector_volatility,
    plot_sector_volatility,
    generate_volatility_insights,
    get_portfolio_weights,
    plot_portfolio
)

def show_sector():
    st.title("📊 Sector Correlation Analysis")

    # -------------------------------
    # CORRELATION
    # -------------------------------
    corr = get_sector_correlation()

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = plot_sector_correlation(corr)
        st.pyplot(fig)

    with col2:
        st.subheader("📌 Key Insights")

        insights = generate_insights(corr)

        for ins in insights:
            st.write(ins)

        st.markdown("---")
        st.subheader("🧠 Interpretation")

        st.write("""
        • High correlation → sectors move together  
        • Low correlation → diversification  
        • Banking, Infra, Energy → macro cluster  
        • IT, FMCG → defensive sectors  
        """)

    # -------------------------------
    # VOLATILITY
    # -------------------------------
    st.markdown("---")
    st.subheader("📈 Sector Volatility Analysis")

    vol = get_sector_volatility()

    col3, col4 = st.columns([2, 1])

    with col3:
        fig2 = plot_sector_volatility(vol)
        st.pyplot(fig2)

    with col4:
        st.subheader("⚠️ Risk Insights")

        vol_insights = generate_volatility_insights(vol)

        for ins in vol_insights:
            st.write(ins)

    # -------------------------------
    # PORTFOLIO
    # -------------------------------
    st.markdown("---")
    st.subheader("📊 Recommended Portfolio Allocation")

    weights = get_portfolio_weights(corr, vol)

    fig3 = plot_portfolio(weights)
    st.pyplot(fig3)


# RUN APP
show_sector()