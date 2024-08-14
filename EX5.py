import streamlit as st

st.title("Cardápio")
st.write("Qual será seu pedido:")
st.write("101 - Cachorro Quente: R$ 8,50")
st.write("102 - Bauru Simples: R$ 4,50")
st.write("104 - Hambúrguer: R$ 5,50")
st.write("105 - Cheeseburguer: R$ 6,60")
st.write("106 - Refrigerante: R$ 6,00")

st.sidebar.header("Informe os seguintes itens:")
compras = 0 

while True:
    codigo = st.sidebar.number_input("Digite qual o código do seu pedido:", min_value=101, max_value=106, step=1)
    quant = st.sidebar.number_input("Quantos itens você deseja?", min_value=1, step=1)

    if codigo == 101:
        compras += quant * 8.50
    elif codigo == 102:
        compras += quant * 4.50
    elif codigo == 104:
        compras += quant * 5.50
    elif codigo == 105:
        compras += quant * 6.60
    elif codigo == 106:
        compras += quant * 6.00

    add = st.sidebar.radio("Deseja adicionar mais algum item?", options=(1, 2), format_func=lambda x: "Sim" if x == 1 else "Não")

    if add == 2:
        break

if st.sidebar.button("Calcular"):
    st.write(f"O valor total da compra é: R$ {compras:.2f}")

