import streamlit as st

st.set_page_config(page_title="Lookify", layout="wide")

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background:#f5f2fb;
    font-family:sans-serif;
}

/* REMOVE */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* SIDES */
.block-container{
    padding-top:1rem;
    padding-bottom:4rem;
}

/* CARD */
.card{
    background:white;
    border-radius:24px;
    padding:18px;
    box-shadow:0 4px 20px rgba(0,0,0,0.05);
    margin-bottom:18px;
}

.section-title{
    font-size:22px;
    font-weight:800;
    color:#1f1b2d;
    margin-bottom:15px;
}

.logo{
    font-size:38px;
    font-weight:900;
    color:#1f1b2d;
}

.subtitle{
    color:#6b7280;
    font-size:15px;
}

.mini-title{
    font-size:14px;
    color:#6b7280;
    font-weight:600;
}

.look-title{
    font-size:22px;
    font-weight:800;
    color:#1f1b2d;
}

.button-purple button{
    background:#8b5cf6;
    color:white;
    border:none;
    border-radius:14px;
}

.quick-card{
    background:#faf7ff;
    border-radius:20px;
    padding:16px;
    text-align:center;
    border:1px solid #ede9fe;
    min-height:120px;
}

.quick-icon{
    font-size:30px;
}

.quick-text{
    font-size:14px;
    font-weight:700;
    margin-top:10px;
    color:#1f1b2d;
}

.product-card{
    background:white;
    border-radius:18px;
    padding:10px;
    border:1px solid #ececec;
}

.product-title{
    font-size:13px;
    font-weight:700;
    color:#111827;
}

.product-price{
    color:#111827;
    font-size:14px;
    font-weight:800;
}

.small-purple{
    color:#8b5cf6;
    font-size:12px;
    font-weight:700;
}

.info-card{
    background:white;
    border-radius:18px;
    padding:14px;
    margin-bottom:12px;
    border:1px solid #ececec;
}

.info-title{
    font-weight:700;
    color:#1f1b2d;
}

.info-sub{
    color:#6b7280;
    font-size:13px;
}

.plus-card{
    background:linear-gradient(135deg,#ede9fe,#ddd6fe);
    border-radius:24px;
    padding:20px;
}

.bottom-nav{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:white;
    border-top:1px solid #ececec;
    display:flex;
    justify-content:space-around;
    padding:12px;
}

.nav-item{
    text-align:center;
    font-size:12px;
    color:#6b7280;
}

.active{
    color:#8b5cf6;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ================= LAYOUT =================
left, right = st.columns([1,1])

# ================= LEFT =================
with left:

    st.markdown("""
    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="font-size:26px;">☰</div>
        <div class="logo">lookify</div>
        <div style="font-size:22px;">🔔</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div style="font-size:24px;font-weight:800;color:#1f1b2d;">
        Bom dia, Júlia! 👋
    </div>

    <div class="subtitle">
        Clima em São Paulo: 18°C ⛅
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # LOOK CARD
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns([1,1])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div class="mini-title">✨ LOOK DO DIA</div>
        <br>
        <div class="look-title">Look casual</div>

        <div class="subtitle">
        Perfeito para seu dia na faculdade
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.button("Ver look completo")

    st.markdown('</div>', unsafe_allow_html=True)

    # ACESSO RAPIDO
    st.markdown('<div class="section-title">Acesso rápido</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="quick-card">
            <div class="quick-icon">✨</div>
            <div class="quick-text">Montar look</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="quick-card">
            <div class="quick-icon">👕</div>
            <div class="quick-text">Meu armário</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="quick-card">
            <div class="quick-icon">🛍️</div>
            <div class="quick-text">Sugestões</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="quick-card">
            <div class="quick-icon">📅</div>
            <div class="quick-text">Calendário</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # PRODUTOS
    st.markdown('<div class="section-title">Sugestões para você</div>', unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1541099649105-f69ad21f3246", use_container_width=True)
        st.markdown('<div class="product-title">Trench coat bege</div>', unsafe_allow_html=True)
        st.markdown('<div class="product-price">R$ 129,90</div>', unsafe_allow_html=True)
        st.markdown('<div class="small-purple">Patrocinado</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with p2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1542291026-7eec264c27ff", use_container_width=True)
        st.markdown('<div class="product-title">Bota de couro</div>', unsafe_allow_html=True)
        st.markdown('<div class="product-price">R$ 179,90</div>', unsafe_allow_html=True)
        st.markdown('<div class="small-purple">Patrocinado</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with p3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1584917865442-de89df76afd3", use_container_width=True)
        st.markdown('<div class="product-title">Bolsa marrom</div>', unsafe_allow_html=True)
        st.markdown('<div class="product-price">R$ 89,90</div>', unsafe_allow_html=True)
        st.markdown('<div class="small-purple">Patrocinado</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ================= RIGHT =================
with right:

    st.markdown('<div class="section-title">O que deseja fazer hoje?</div>', unsafe_allow_html=True)

    r1, r2 = st.columns(2)

    with r1:
        st.markdown("""
        <div class="card">
            <div style="font-size:30px;">✨</div>
            <br>
            <div class="info-title">Montar look do dia</div>
            <div class="info-sub">
            Nossa IA cria o look perfeito para você.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with r2:
        st.markdown("""
        <div class="card">
            <div style="font-size:30px;">👕</div>
            <br>
            <div class="info-title">Editar peças</div>
            <div class="info-sub">
            Adicione, edite ou remova roupas.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="section-title">Outras opções importantes</div>', unsafe_allow_html=True)

    options = [
        ("📊", "Estatísticas do armário"),
        ("🔖", "Looks salvos"),
        ("❤️", "Favoritos"),
        ("☁️", "Clima e ocasiões"),
        ("🤖", "IA conversacional")
    ]

    for icon, title in options:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-title">{icon} {title}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="plus-card">
        <div style="font-size:28px;font-weight:800;color:#6d28d9;">
            Lookify Plus ✨
        </div>

        <br>

        <div style="color:#4b5563;">
            Tenha acesso ilimitado às funcionalidades premium.
        </div>

        <br>

        <div style="
            background:#8b5cf6;
            color:white;
            width:160px;
            text-align:center;
            padding:12px;
            border-radius:14px;
            font-weight:700;
        ">
            Assinar agora
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="bottom-nav">
    <div class="nav-item active">🏠<br>Início</div>
    <div class="nav-item">👕<br>Armário</div>
    <div class="nav-item">✨<br>IA</div>
    <div class="nav-item">🛍️<br>Marketplace</div>
    <div class="nav-item">👤<br>Perfil</div>
</div>
""", unsafe_allow_html=True)
