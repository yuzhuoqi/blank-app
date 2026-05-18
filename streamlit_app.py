import streamlit as st

st.set_page_config(
    page_title="Lookify",
    layout="centered"
)

# ===== CSS =====
st.markdown("""
<style>

.stApp{
    background-color:#f5f5f7;
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
    color:#111827;
    margin-bottom:0;
}

.top-text{
    color:#6b7280;
    font-size:16px;
}

/* MAIN CARD */
.main-card{
    background:white;
    border-radius:28px;
    padding:22px;
    box-shadow:0 4px 20px rgba(0,0,0,0.05);
    margin-bottom:25px;
}

.look-title{
    font-size:24px;
    font-weight:800;
    color:#111827;
}

.look-sub{
    color:#6b7280;
    font-size:15px;
}

.temp{
    background:#8b5cf6;
    color:white;
    padding:6px 14px;
    border-radius:999px;
    font-size:14px;
    font-weight:600;
}

.section-title{
    font-size:24px;
    font-weight:800;
    color:#111827;
    margin-top:10px;
    margin-bottom:15px;
}

/* QUICK ACCESS */
.quick-card{
    background:white;
    border-radius:20px;
    padding:18px;
    text-align:center;
    box-shadow:0 4px 15px rgba(0,0,0,0.05);
}

.quick-icon{
    font-size:28px;
}

.quick-text{
    font-size:14px;
    font-weight:600;
    margin-top:10px;
}

/* PRODUCT CARD */
.product-card{
    background:white;
    border-radius:20px;
    padding:12px;
    box-shadow:0 4px 15px rgba(0,0,0,0.05);
}

.product-title{
    font-size:14px;
    font-weight:700;
    color:#111827;
}

.product-price{
    color:#111827;
    font-weight:700;
    margin-top:5px;
}

.sponsor{
    background:#ede9fe;
    color:#7c3aed;
    padding:4px 10px;
    border-radius:999px;
    font-size:11px;
    width:fit-content;
    margin-top:8px;
}

/* FOOTER NAV */
.bottom-nav{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:white;
    padding:15px;
    border-top:1px solid #e5e7eb;
    display:flex;
    justify-content:space-around;
}

.nav-item{
    text-align:center;
    color:#6b7280;
    font-size:12px;
}

.active{
    color:#7c3aed;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown(
    """
    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="font-size:28px;">☰</div>
        <div class="logo">lookify</div>
        <div style="font-size:24px;">🔔</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div style="font-size:34px;font-weight:800;color:#111827;">
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
    """
    <div class="main-card">

        <div style="display:flex;justify-content:space-between;align-items:center;">
            <div>
                <div style="color:#7c3aed;font-weight:700;">
                    ✨ LOOK DO DIA
                </div>

                <div class="look-sub">
                    Baseado no clima e na sua rotina
                </div>
            </div>

            <div class="temp">
                18°C
            </div>
        </div>

        <br>

        <div style="display:flex;gap:20px;align-items:center;">

            <img src="https://images.unsplash.com/photo-1529139574466-a303027c1d8b"
            width="180"
            style="border-radius:20px;">

            <div>
                <div class="look-title">
                    Look casual
                </div>

                <div class="look-sub">
                    Perfeito para sua rotina na faculdade
                </div>

                <br>

                <button style="
                    background:#8b5cf6;
                    color:white;
                    border:none;
                    padding:12px 18px;
                    border-radius:16px;
                    font-weight:700;
                    cursor:pointer;
                ">
                    Ver look completo
                </button>
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)

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

# ===== SUGESTOES =====
st.markdown(
    '<div class="section-title">Sugestões para você</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="product-card">
        <img src="https://images.unsplash.com/photo-1541099649105-f69ad21f3246"
        width="100%" style="border-radius:16px;">

        <div class="product-title">
            Trench coat bege
        </div>

        <div class="product-price">
            R$ 129,90
        </div>

        <div class="sponsor">
            Patrocinado
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="product-card">
        <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff"
        width="100%" style="border-radius:16px;">

        <div class="product-title">
            Bota de couro
        </div>

        <div class="product-price">
            R$ 179,90
        </div>

        <div class="sponsor">
            Patrocinado
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="product-card">
        <img src="https://images.unsplash.com/photo-1584917865442-de89df76afd3"
        width="100%" style="border-radius:16px;">

        <div class="product-title">
            Bolsa marrom
        </div>

        <div class="product-price">
            R$ 89,90
        </div>

        <div class="sponsor">
            Patrocinado
        </div>
    </div>
    """, unsafe_allow_html=True)

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
