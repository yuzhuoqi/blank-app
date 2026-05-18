import streamlit as st

st.set_page_config(
    page_title="Lookify",
    layout="centered"
)

# ===== CSS =====
st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#eef7ff,#dbeafe);
    font-family:sans-serif;
}

/* REMOVE MENU */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* HEADER */
.logo{
    font-size:42px;
    font-weight:900;
    color:#0f172a;
    margin-bottom:0;
}

.top-text{
    color:#475569;
    font-size:16px;
}

/* TITLES */
.section-title{
    font-size:24px;
    font-weight:800;
    color:#0f172a;
    margin-top:10px;
    margin-bottom:15px;
}

.look-title{
    font-size:28px;
    font-weight:800;
    color:#0f172a;
}

.look-sub{
    color:#475569;
    font-size:16px;
    line-height:1.6;
}

/* CARDS */
.card{
    background:rgba(255,255,255,0.75);
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.4);
    border-radius:28px;
    padding:20px;
    box-shadow:0 8px 30px rgba(59,130,246,0.10);
}

/* QUICK ACCESS */
.quick-card{
    background:rgba(255,255,255,0.8);
    border-radius:22px;
    padding:18px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.5);
    box-shadow:0 8px 20px rgba(59,130,246,0.08);
    transition:0.3s;
}

.quick-card:hover{
    transform:translateY(-3px);
}

.quick-icon{
    font-size:28px;
}

.quick-text{
    font-size:14px;
    font-weight:700;
    margin-top:10px;
    color:#0f172a;
}

/* PRODUCT CARD */
.product-card{
    background:rgba(255,255,255,0.85);
    border-radius:22px;
    padding:12px;
    border:1px solid rgba(255,255,255,0.5);
    box-shadow:0 8px 20px rgba(59,130,246,0.08);
}

.product-title{
    font-size:14px;
    font-weight:700;
    color:#0f172a;
}

.product-price{
    color:#2563eb;
    font-weight:800;
    margin-top:5px;
}

/* BUTTON */
.stButton button{
    background:linear-gradient(135deg,#60a5fa,#38bdf8);
    color:white;
    border:none;
    border-radius:18px;
    padding:12px 18px;
    font-weight:700;
    box-shadow:0 8px 20px rgba(59,130,246,0.25);
    transition:0.3s;
}

.stButton button:hover{
    transform:scale(1.02);
}

/* FOOTER */
.bottom-nav{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:rgba(255,255,255,0.8);
    backdrop-filter:blur(12px);
    padding:15px;
    border-top:1px solid rgba(255,255,255,0.5);
    display:flex;
    justify-content:space-around;
}

.nav-item{
    text-align:center;
    color:#64748b;
    font-size:12px;
}

.active{
    color:#3b82f6;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown(
    """
    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="font-size:28px;color:#64748b;">☰</div>
        <div class="logo">lookify</div>
        <div style="font-size:24px;">🔔</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div style="font-size:34px;font-weight:800;color:#0f172a;">
        Bom dia, Julia! 👋
    </div>

    <div class="top-text">
        Clima em São Paulo: 18°C ⛅
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ===== LOOK DO DIA =====
st.markdown(
    '<div class="section-title">✨ LOOK DO DIA</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
        use_container_width=True
    )

with col2:

    st.markdown(
        """
        <div class="look-title">
            Look casual
        </div>

        <br>

        <div class="look-sub">
            Perfeito para sua rotina na faculdade
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.button("Ver look completo")

st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# ===== ACESSO RAPIDO =====
st.markdown(
    '<div class="section-title">Acesso rápido</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="quick-card">
        <div class="quick-icon">✨</div>
        <div class="quick-text">Montar look</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="quick-card">
        <div class="quick-icon">👕</div>
        <div class="quick-text">Meu armário</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="quick-card">
        <div class="quick-icon">🛍️</div>
        <div class="quick-text">Sugestões</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="quick-card">
        <div class="quick-icon">📅</div>
        <div class="quick-text">Calendário</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ===== SUGESTÕES =====
st.markdown(
    '<div class="section-title">Sugestões para você</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1541099649105-f69ad21f3246",
        use_container_width=True
    )
    st.markdown("**Trench coat bege**")
    st.markdown('<div class="product-price">R$ 129,90</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
        use_container_width=True
    )
    st.markdown("**Bota de couro**")
    st.markdown('<div class="product-price">R$ 179,90</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1584917865442-de89df76afd3",
        use_container_width=True
    )
    st.markdown("**Bolsa marrom**")
    st.markdown('<div class="product-price">R$ 89,90</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# ===== FOOTER =====
st.markdown("""
<div class="bottom-nav">
    <div class="nav-item active">🏠<br>Início</div>
    <div class="nav-item">👕<br>Armário</div>
    <div class="nav-item">✨<br>IA</div>
    <div class="nav-item">🛍️<br>Marketplace</div>
    <div class="nav-item">👤<br>Perfil</div>
</div>
""", unsafe_allow_html=True)
