import streamlit as st

st.set_page_config(page_title="LookFy", layout="centered")

# ===== ESTILO =====
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0b0d;
        color: white;
    }

    .main-title {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        color: #9ca3af;
        margin-top: 0;
        margin-bottom: 30px;
    }

    .hero {
        background: linear-gradient(135deg, #1f1f22, #000000);
        padding: 30px;
        border-radius: 30px;
        border: 1px solid #2f2f35;
        margin-bottom: 30px;
        box-shadow: 0px 0px 30px rgba(255,255,255,0.05);
    }

    .hero-title {
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .hero-text {
        color: #c4c4c4;
        line-height: 1.6;
        font-size: 16px;
    }

    .card {
        background: #141416;
        padding: 24px;
        border-radius: 28px;
        border: 1px solid #2a2a2f;
        margin-bottom: 20px;
        transition: 0.3s;
        box-shadow: 0px 0px 20px rgba(255,255,255,0.03);
    }

    .card:hover {
        transform: scale(1.02);
        border: 1px solid #4b5563;
    }

    .look-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 12px;
    }

    .look-tags {
        color: #d4d4d8;
        line-height: 1.8;
        font-size: 15px;
    }

    .footer {
        text-align: center;
        color: #71717a;
        margin-top: 40px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ===== HEADER =====
st.markdown(
    '<p class="main-title">LookFy ✨</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Fashion AI Experience</p>',
    unsafe_allow_html=True
)

# ===== HERO =====
st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            O look ideal para hoje.
        </div>

        <div class="hero-text">
            A IA analisou seu armário, o clima e seu estilo
            para criar combinações perfeitas para o seu dia.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== BOTÃO =====
if st.button("✨ Gerar Look"):
    st.success("IA criando combinações personalizadas...")

# ===== LOOKS =====
looks = [
    {
        "nome": "Look Casual",
        "emoji": "🖤",
        "tags": ["Jaqueta preta", "Camiseta branca", "Calça cargo"]
    },
    {
        "nome": "Look Festa",
        "emoji": "✨",
        "tags": ["Vestido preto", "Bolsa prata", "Salto alto"]
    },
    {
        "nome": "Look Trabalho",
        "emoji": "💼",
        "tags": ["Blazer oversized", "Calça alfaiataria", "Tênis branco"]
    }
]

st.subheader("Looks sugeridos")

for look in looks:

    tags = " • ".join(look["tags"])

    st.markdown(
        f"""
        <div class="card">
            <div class="look-title">
                {look['emoji']} {look['nome']}
            </div>

            <div class="look-tags">
                {tags}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===== FOOTER =====
st.markdown(
    '<div class="footer">LookFy • Projeto de Faculdade • Fashion Tech + IA</div>',
    unsafe_allow_html=True
)
