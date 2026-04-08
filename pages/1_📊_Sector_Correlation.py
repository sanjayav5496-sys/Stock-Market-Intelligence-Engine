import streamlit as st
from sector_correlation import (
    get_sector_correlation,
    plot_sector_correlation,
    generate_insights
)

def show_sector():
    st.title("📊 Sector Correlation Analysis")

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


show_sector()