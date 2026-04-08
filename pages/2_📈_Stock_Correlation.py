import streamlit as st
from stock_correlation import (
    get_stock_correlation,
    plot_stock_correlation,
    generate_stock_insights
)

def show_stock():
    st.title("📈 Stock Correlation Analysis")

    corr = get_stock_correlation()

    col1, col2 = st.columns([2, 1])

    # LEFT → Heatmap
    with col1:
        fig = plot_stock_correlation(corr)
        st.pyplot(fig)

    # RIGHT → Insights
    with col2:
        st.subheader("📌 Key Insights")

        insights = generate_stock_insights(corr)

        for ins in insights:
            st.write(ins)

        st.markdown("---")
        st.subheader("🧠 Interpretation")

        st.write("""
        • High correlation → avoid holding both stocks heavily  
        • Low correlation → helps diversification  
        • Same sector stocks → usually highly correlated  
        • Cross-sector picks → better portfolio balance  
        """)

show_stock()