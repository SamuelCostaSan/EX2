import streamlit as st

st.title("Calcule Dia, Mês e Ano")
st.sidebar.header("Necessito de Informações")

nascimento = st.sidebar.number_input("Em que ano você nasceu?", min_value=1900, max_value=2100, step=1)
atual = st.sidebar.number_input("Em que ano estamos?", min_value=1900, max_value=2100, step=1)

calcular_b = st.sidebar.button("Calcular")

if calcular_b:
    ano = atual - nascimento
    mes = ano * 12
    dia = ano * 365
    st.success(f'Você tem {ano} anos, {mes} mês(es) e {dia} dia(s) aproximadamente')
