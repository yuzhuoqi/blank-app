# Interface da tela “Look” — Lookify

```python
import streamlit as st

st.set_page_config(
    page_title="Lookify - Look",
    layout="centered"
)

# ===== CSS =====
st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#f8f4ff,#efe7ff);
    font-family:sans-serif;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.logo{
    font-size:40px;
    font-weight:900;
    color:#2e1065;
}

.page-title{
    font-size:34px;
    font-weight:800;
    color:#2e1065;
    margin-top:10px;
}

.subtitle{
    color:#6d5b8c;
    font-size:16px;
    margin-bottom:20px;
}

.look-card{
    background:rgba(255,255,255,0.82);
    border-radius:28px;
    padding:18px;
    border:1px solid rgba(255,255,255,0.5);
    box-shadow:0 8px 20px rgba(168,85,247,0.08);
    margin-bottom:25px;
}

.look-name{
    font-size:24px;
    font-weight:800;
    color:#2e1065;
    margin-top:12px;
}

.look-desc{
    color:#6d5b8c;
    font-size:15px;
    line-height:1.6;
}

.section-title{
    font-size:24px;
    font-weight:800;
    color:#2e1065;
    margin-bottom:15px;
}

.tag{
    background:#e9d5ff;
    color:#7e22ce;
    padding:8px 14px;
    border-radius:999px;
    font-size:13px;
    font-weight:700;
    display:inline-block;
    margin-right:8px;
    margin-bottom:8px;
}

.product-card{
    background:rgba(255,255,255,0.82);
    border-radius:22px;
    padding:12px;
    border:1px solid rgba(255,255,255,0.5);
    box-shadow:0 8px 20px rgba(168,85,247,0.08);
}

.product-title{
    font-size:14px;
    font-weight:700;
    color:#111827;
}

.product-price{
    color:#111827;
    font-weight:800;
    margin-top:5px;
}

.stButton button{
    background:linear-gradient(135deg,#c084fc,#a855f7);
    color:white;
    border:none;
    border-radius:18px;
    padding:12px 18px;
    font-weight:700;
    box-shadow:0 8px 20px rgba(168,85,247,0.20);
    transition:0.3s;
}

.stButton button:hover{
    transform:scale(1.02);
}

.bottom-nav{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:rgba(255,255,255,0.75);
    backdrop-filter:blur(12px);
    padding:15px;
    border-top:1px solid rgba(255,255,255,0.5);
    display:flex;
    justify-content:space-around;
}

.nav-item{
    text-align:center;
    color:#7c6a99;
    font-size:12px;
}

.active{
    color:#9333ea;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown(
    """
    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div style="font-size:28px;color:#7c6a99;">←</div>
        <div class="logo">lookify</div>
        <div style="font-size:24px;">♡</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <div class="page-title">
        Look do dia ✨
    </div>

    <div class="subtitle">
        Selecionado pela IA baseado no clima e no seu estilo.
    </div>
    """,
    unsafe_allow_html=True
)

# ===== LOOK PRINCIPAL =====
st.markdown('<div class="look-card">', unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
    use_container_width=True
)

st.markdown(
    """
    <div class="look-name">
        Lavender Casual Fit
    </div>

    <br>

    <div class="look-desc">
        Um visual confortável e moderno para faculdade,
        encontros ou rotina do dia a dia.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <span class="tag">Casual</span>
    <span class="tag">Minimalista</span>
    <span class="tag">Street</span>
    <span class="tag">Confortável</span>
    """,
    unsafe_allow_html=True
)

st.write("")

st.button("✨ Gerar outro look", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== PEÇAS DO LOOK =====
st.markdown(
    '<div class="section-title">Peças do look</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1521572267360-ee0c2909d518",
        use_container_width=True
    )
    st.markdown('<div class="product-title">Classic White Tee</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">R$ 79,90</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1542272604-787c3835535d",
        use_container_width=True
    )
    st.markdown('<div class="product-title">Wide Denim Pants</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">R$ 149,90</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
        use_container_width=True
    )
    st.markdown('<div class="product-title">Urban Sneakers</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">R$ 219,90</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# ===== FOOTER =====
st.markdown("""
<div class="bottom-nav">
    <div class="nav-item">🏠<br>Início</div>
    <div class="nav-item active">✨<br>Look</div>
    <div class="nav-item">👕<br>Armário</div>
    <div class="nav-item">🛍️<br>Shop</div>
    <div class="nav-item">👤<br>Perfil</div>
</div>
""", unsafe_allow_html=True)

```
