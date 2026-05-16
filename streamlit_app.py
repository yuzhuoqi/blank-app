import streamlit as st

st.set_page_config(page_title="Lookify", layout="centered")

# ===== ESTILO =====
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0b0d;
        color: white;
    }

    .main-title {
        font-size: 64px;
        font-weight: 900;
        margin-bottom: 0;
        line-height: 1;
    }

    .subtitle {
        color: #9ca3af;
        margin-top: 10px;
        margin-bottom: 35px;
        font-size: 22px;
        font-weight: 500;
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
    }

    .footer {
        text-align: center;
        color: #71717a;
        margin-top: 40px;
        font-size: 14px;
    }

    .stButton button {
        background-color: #141416;
        color: white;
        border: 1px solid #2a2a2f;
        border-radius: 20px;
        padding: 18px;
        font-size: 20px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton button:hover {
        border: 1px solid #4b5563;
        transform: scale(1.01);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ===== HEADER =====
st.markdown(
    '<p class="main-title">Lookify ✨</p>',
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
            Seu estilo, elevado pela IA.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== BOTÃO IA =====
if st.button("✨ Gerar Look"):
    st.success("IA criando combinações personalizadas...")

# ===== LOOKS =====
st.subheader("Looks sugeridos")

looks = {
    "🖤 Look Casual": "Combinação perfeita para o dia a dia.",
    "✨ Look Festa": "Looks elegantes para eventos noturnos.",
    "💼 Look Trabalho": "Visual profissional e moderno.",
    "🏋️ Look Academia": "Conforto e estilo para treinar.",
    "✈️ Look Viagem": "Looks confortáveis para viajar.",
    "📚 Look Faculdade": "Estilo casual para a rotina universitária."
}

for nome, descricao in looks.items():

    if st.button(nome, use_container_width=True):
        st.markdown(
            f'''
            <div class="card">
                <div class="look-title">{nome}</div>
                <br>
                <div style="color:#c4c4c4; font-size:18px;">
                    {descricao}
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )

# ===== FOOTER =====
st.markdown(
    '<div class="footer">Lookify • Projeto de Faculdade • Fashion Tech + IA</div>',
    unsafe_allow_html=True
)
