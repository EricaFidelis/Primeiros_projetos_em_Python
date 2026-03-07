import streamlit as st
import json
import random
from datetime import datetime
import os

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Cofre de Luz", page_icon="✨", layout="centered")

# 2. LÓGICA DE CORES (DINÂMICO)
hora_atual = datetime.now().hour
if 5 <= hora_atual < 12:
    bg_color, accent, text_c = "linear-gradient(180deg, #FFEFBA 0%, #FFFFFF 100%)", "#e67e22", "#5d4037"
    estrela_c = "transparent"
elif 12 <= hora_atual < 18:
    bg_color, accent, text_c = "linear-gradient(180deg, #e0f7fa 0%, #f0f4ff 100%)", "#4db6ac", "#2c3e50"
    estrela_c = "transparent"
else:
    bg_color, accent, text_c = "linear-gradient(180deg, #0f2027 0%, #2c5364 100%)", "#9a8c98", "#ecf0f1"
    estrela_c = "gold"

# 3. CSS E ESTRELAS
st.markdown(f"""
    <style>
    .stApp {{ background: {bg_color}; }}
    .moldura-poetica {{
        font-family: 'Georgia', serif; font-size: 1.4rem; color: {text_c};
        line-height: 1.8; text-align: center; padding: 45px;
        background: rgba(255, 255, 255, 0.1); border-radius: 30px;
        backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);
    }}
    .stButton>button {{
        border-radius: 25px; background: {accent}; color: white; border: none; width: 100%;
    }}
    .feedback-box {{
        background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px;
        text-align: center; border: 1px dashed {accent}; margin-top: 30px;
    }}
    @keyframes pulse {{ 0% {{ opacity: 0.2; }} 50% {{ opacity: 1; }} 100% {{ opacity: 0.2; }} }}
    .estrela {{ position: fixed; color: {estrela_c}; animation: pulse 3s infinite; font-size: 20px; }}
    </style>
    <div class="estrela" style="top:10%; left:15%;">✦</div>
    <div class="estrela" style="top:35%; left:80%;">✦</div>
    <div class="estrela" style="top:75%; left:25%;">✦</div>
    """, unsafe_allow_html=True)

def carregar():
    return json.load(open("diario.json", "r", encoding="utf-8")) if os.path.exists("diario.json") else []
def salvar(d):
    json.dump(d, open("diario.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)

historico = carregar()
if 'aberto' not in st.session_state: st.session_state.aberto = False

# --- TELA 1 (SEU TEXTO FAVORITO - SEM CORTES) ---
if not st.session_state.aberto:
    st.markdown(f"<h1 style='text-align:center; color:{text_c};'>🔐 O Cofre de Luz</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class='moldura-poetica'>
        "A gratidão é a luz que acendemos dentro de nós quando o mundo lá fora parece barulhento e escuro demais. 
        É o ato revolucionário de pausar o caos para reconhecer que, apesar das tempestades, 
        ainda existem portos seguros nos pequenos detalhes: no calor de um café, 
        no abraço de quem amamos ou no fôlego que nos permite recomeçar. 
        É entender que cada esforço silencioso seu tem valor e que, mesmo quando o caminho parece longo, 
        você não está apenas caminhando — você está florescendo. 
        Ser grato é abraçar a própria história com ternura e descobrir que o maior tesouro 
        desse cofre é a coragem que você tem de acreditar na beleza do amanhã."
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar o Espaço de Gratidão ✨"):
        st.session_state.aberto = True
        st.rerun()

# --- TELA 2 ---
else:
    st.markdown(f"<h1 style='text-align:center; color:{text_c};'>✨ Espaço Compartilhado</h1>", unsafe_allow_html=True)
    
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
    st.markdown(f"<p style='text-align:center; color:{accent}; font-weight:bold;'>💡 Já preservamos {len(historico)} momentos de luz.</p>", unsafe_allow_html=True)

    novo = st.text_area("O que trouxe paz ao seu dia?", placeholder="Escreva aqui...")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Guardar Momento 🌿"):
            if novo:
                historico.append({"data": datetime.now().strftime("%d/%m/%Y"), "texto": novo})
                salvar(historico)
                st.balloons()
                st.success("Guardado!")
            else: st.warning("Escreva algo primeiro.")
    with c2:
        if st.button("Inspirar-se 🌟"):
            if historico:
                rec = random.choice(historico)
                st.info(f"\"{rec['texto']}\"")

    st.markdown("---")
    st.markdown(f"""
        <div class="feedback-box">
            <h4 style="color:{text_c};">Dúvidas ou Sugestões?</h4>
            <a href="mailto:ericafidelis445@gmail.com?subject=Feedback - Cofre de Luz" 
               style="color:{accent}; text-decoration: none; font-weight: bold; font-size: 1.1rem;">
               ericafidelis445@gmail.com ✉️
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Fechar Cofre 🔒"):
        st.session_state.aberto = False
        st.rerun()