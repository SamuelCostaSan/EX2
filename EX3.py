import streamlit as st

def calcula_desconto(preco, codigo_regiao):
    descontos = {
        1: 0.05,  
        2: 0.15,  
        3: 0.07,  
        4: 0.12,
        5: 0.20,  
    }
    
    if codigo_regiao in descontos:
        taxa_desconto = descontos[codigo_regiao]
        desconto = preco * taxa_desconto
        preco_final = preco - desconto
        return desconto, preco_final
    else:
        return None, None

st.title("Calculadora de Desconto")
preco = st.number_input("Preço do produto (em reais)", min_value=0.0, format="%.2f")
codigo_regiao = st.number_input("Código da região", min_value=1, max_value=5, step=1)

if st.button("Calcular Desconto"):
    desconto, preco_final = calcula_desconto(preco, codigo_regiao)
    if desconto is None:
        st.write("Código da região inválido.")
    else:
        st.write(f"Desconto: R$ {desconto:.2f}")
        st.write(f"Preço final com desconto: R$ {preco_final:.2f}")
