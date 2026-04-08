import streamlit as st

st.set_page_config(page_title="Stock Market Intelligence Engine", layout="wide")

# ---------- PREMIUM CSS ----------
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top, #0b1f17, #05070d);
}

/* Center alignment */
.center {
    text-align: center;
}

/* Title */
.title {
    font-size: 55px;
    font-weight: bold;
    color: #00FF9C;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #9CA3AF;
    margin-top: 12px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

/* Card Button Style */
.card {
    background: linear-gradient(145deg, #111827, #0E1117);
    padding: 30px;
    border-radius: 16px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 1px solid rgba(0,255,150,0.2);
}

/* Hover Glow Effect */
.card:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 0 25px rgba(0,255,150,0.4),
                0 0 50px rgba(0,255,150,0.2);
    border: 1px solid rgba(0,255,150,0.6);
}

/* Card title */
.card-title {
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
st.markdown("""
<div class="center">
    <div class="title">📊 Stock Market Intelligence Engine</div>
    <div class="subtitle">
        Advanced Market Intelligence Engine for decoding sector dynamics, stock relationships,<br>
        and macro influences through data-driven insights.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- FEATURE CARDS ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🔗 Sector Analysis</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🔥 Stock Correlation</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">🪙 Commodity Analysis</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-title">⚖️ Risk Optimization</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- FOOTER ----------
st.markdown("""
<div class="center subtitle">
Built to uncover hidden relationships between sectors, stocks, and commodities — enabling smarter and data-driven investment decisions.
</div>
""", unsafe_allow_html=True)